import logging
import database_service as dbs
import api_service as aps

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

LOCATION_MULT, CONTINUE = range(2)

def start_multiple(update: Update, context: CallbackContext) -> int:

    context.user_data["data"] = {}

    reply_keyboard = [["A lot", "Medium", "Low", "Nothing at all"]]

    update.message.reply_text(
        'Thanks for taking part in this\n'
        'How crowded is the area you are in?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Crowded'
        ),
    )    

    context.user_data["data"]["typeOfData"] = "crowdedness"    

    return CONTINUE

def continue_(update: Update, context: CallbackContext) -> int:    
    
    context.user_data["data"]["value"] = update.message.text     

    update.message.reply_text(
        'Now send your position!'        
    )
    
    return LOCATION_MULT

def location_mult(update: Update, context: CallbackContext) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    context.user_data["data"]["id"] = str(user.id)
    context.user_data["data"]["consumerType"] = "telegrambot"
    context.user_data["data"]["position"] = {"longitude": user_location.longitude, "latitude": user_location.latitude}

    points = dbs.add_points_user(user.id, 100)
    update.message.reply_text(
        'Thanks for sharing!\n'
        'You received 100 points for your participation\n'
        'Keep up the good work champ! \n'  
        'Total points: ' + str(points[0])     
    )    

    aps.send_data(context.user_data["data"])

    return ConversationHandler.END
