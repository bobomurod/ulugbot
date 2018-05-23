from telegram.ext import Updater
updater = Updater(token='579664849:AAGzf4g6bWtzuE5L2qZygi3Cq39PrlZVxuc')
dispatcher = updater.dispatcher
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):bot.send_message(chat_id=update.message.chat_id, text="Ya bot, pogovori so mnoy")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def caps(bot, update, args):
        text_caps = ' '.join(args).upper()
        bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

def some_func(args):
        myArg = args
        bot.send_message(chat_id=update.message.chat_id, text=myArg)

some_func_handler = MessageHandler(some_func)
dispatcher.add_handler(some_func_handler)

updater.start_polling()

