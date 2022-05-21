#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

from http.client import CONTINUE
import logging
import database_service as dbs
import bot_photo_question as bpq
import bot_mult_question as bmq

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ParseMode, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    JobQueue,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

PHOTO, LOCATION = range(2)
LOCATION_MULT, CONTINUE = range(2)

def start(update: Update, context: CallbackContext) -> int:    
    """Send a message when the command /start is issued."""    
    user = update.effective_user
    dbs.check_user(user.id)
    update.message.reply_text(
        "User added to the database " + str(user.id) + " "
    )    

def check_news(context):
    """Send a message if there are any news"""       

    res = dbs.get_new_question()
    if(res is not None):

        print(res[3].split(",")[0])

        text_base = "Hi, we have a new question for you!\n"
        text_base += "If you want to answer it, please send /confirm" + res[3].split(",")[0] + " and follow the instructions\n"
        text_base += "Here is the question: \n\n _"

        for x in dbs.get_all_users():
            chat_id = x[0]                        
            context.bot.send_message(chat_id, text= text_base + res[1] + "_ \n",
                            parse_mode=ParseMode.MARKDOWN)

def help(update: Update, context: CallbackContext) -> int:    
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "La descrizione piu bella del mondo"
    )    

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def ranking(update: Update, context: CallbackContext) -> int:    
    """Send a message when the command /ranking is issued."""
    res = dbs.get_ranking()
    text = ""
    for x in res:
        text += "User: " + str(x[0]) + " with " + str(x[1]) + " points\n"
    update.message.reply_text(
        "The ranking is: \n\n" + text 
    )

def main() -> None:
    """Run the bot."""
    
    # Create the Updater and pass it your bot's token.
    TOKEN = "5382382091:AAGJhB3_nOLIf38L4t8Xn6xgtUcBvwhf960"    
    updater = Updater(TOKEN)

    bot = updater.bot
    dispatcher = updater.dispatcher
    job_queue = updater.job_queue    

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler_photo = ConversationHandler(
        entry_points=[CommandHandler('confirmphoto', bpq.start_photo)],
        states={
            PHOTO: [MessageHandler(Filters.photo, bpq.photo)],
            LOCATION: [
                MessageHandler(Filters.location, bpq.location),                
            ]            
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    conv_handler_multiple = ConversationHandler(
        entry_points=[CommandHandler('confirmmult', bmq.start_multiple)],
        states={ 
            CONTINUE: [MessageHandler(Filters.text, bmq.continue_)],      
            LOCATION_MULT: [
                MessageHandler(Filters.location, bmq.location_mult),                
            ]            
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler_photo)    
    dispatcher.add_handler(conv_handler_multiple)    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))  
    dispatcher.add_handler(CommandHandler("ranking", ranking))    

    # run repeatedly    
    job_queue.run_repeating(check_news, interval=6, first=0)

    # Start the Bot
    updater.start_polling()    
    
    updater.idle()    

if __name__ == '__main__':
    main()