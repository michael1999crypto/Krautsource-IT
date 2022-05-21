import logging
import database_service as dbs

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

PHOTO, LOCATION = range(2)

def start_photo(update: Update, context: CallbackContext) -> int:    
    update.message.reply_text(
        'Thanks for taking part in this\n'
        'Start by sending the photo you were requested to send'            
    )

    return PHOTO

def photo(update: Update, context: CallbackContext) -> int:

    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text(
        'Gorgeous! Now, send me the location of the photo'
    )

    return LOCATION

def location(update: Update, context: CallbackContext) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    points = dbs.add_points_user(user.id, 100)
    update.message.reply_text(
        'Thanks for sharing!'
        'You received 100 points for your participation'
        'Keep up the good work champ!'  
        'Total points: ' + str(points[0])     
    )
    update.message.reply_photo(open('predictions.jpg', 'rb'))

    return ConversationHandler.END
