from telegram.ext import Updater
updater = Updater(token='579664849:AAGzf4g6bWtzuE5L2qZygi3Cq39PrlZVxuc')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):bot.send_message(chat_id=update.message.chat_id, text="Ya bot, pogovori so mnoy")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

