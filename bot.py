import logging
import os

import requests
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from tests import finder
import datase



PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'USER TOKEN'


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    menu_keyboard = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K', 'L'], ['M', 'N'], ['O', 'P'],
                     ['Q', 'R'], ['S', 'T'], ['U', 'V'], ['W', 'X'], ['Y', 'Z'],
                     ]

    menu_markup = telegram.ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=False)
    update.message.reply_text('Select Country!', reply_markup=menu_markup)
    contents = requests.get('https://api.covid19api.com/summary').json()
    global countries
    countries = contents["Countries"]


#    """Send a message when the command /start is issued."""
# keyboard = [[telegram.InlineKeyboardButton("Option 1", callback_data='1'),
#             telegram.InlineKeyboardButton("Option 2", callback_data='2'),
#            telegram.InlineKeyboardButton("Option 4", callback_data='4')],
#
#               [telegram.InlineKeyboardButton("Option 3", callback_data='3')]]

#  reply_markup = telegram.InlineKeyboardMarkup(keyboard)

# update.message.reply_text('Updates from ' + user_country, reply_markup=reply_markup)


# update.user.get_profile_photos('https://media.wired.com/photos/5b899992404e112d2df1e94e/master/pass/trash2-01.jpg')

def help(update, context):
    #    """Send a message when the command /help is issued."""
    #    menu_keyboard = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K', 'L'], ['M', 'N'], ['O', 'P'],
    #                     ['Q', 'R'],
    #                    ['S', 'T'], ['U', 'V'], ['W', 'X'], ['Y', 'Z'],
    #                    ]

    #    menu_markup = telegram.ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=False)

    update.message.reply_text('Enter "/start" to reconfigure settings')


def echo(update, context):
    arr = ['New Recoveries', 'New Confirmed', 'New Deaths',
                             'Total Recoveries', 'Total Confirmed', 'Total Deaths',
                             ]
    if (len(update.message.text) < 2):
        a_keyboard = finder(update.message.text)
        a_markup = telegram.ReplyKeyboardMarkup(a_keyboard, one_time_keyboard=True, resize_keyboard=False)
        update.message.reply_text(update.message.text + ' Countries', reply_markup=a_markup)


    elif (update.message.text not in arr):
        global countryCode
        countryCode = datase.findInv(countries, update.message.text)

        menu_keyboard = [['New Recoveries'], ['New Confirmed'], ['New Deaths'],
                         ['Total Recoveries'], ['Total Confirmed'], ['Total Deaths'],
                             ]
        menu_markup = telegram.ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=False)
        update.message.reply_text('Updates from ' + update.message.text,
                                  reply_markup=menu_markup)
    else:
        send = datase.choice_to_number(update.message.text, countries, countryCode)
        print(send)
        update.message.reply_text(send)
    """Echo the user message."""


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
