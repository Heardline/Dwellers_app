import sys
import os
import logging
import django
from typing import Dict

from django.conf import settings
import telegram.error
from telegram import Bot, Update, BotCommand
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler,
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")
django.setup()


from tgbot.handlers.comman import command_start

log = logging.getLogger(__name__)

def setup_dispatcher(dp):

    #=============================Handlers====================================
    dp.add_handler(CommandHandler("start", command_start))

    #dp.add_error_handler(error.send_stacktrace_to_tg_chat)
    return dp

def main() -> None:
    """ Run bot in pooling mode """
  
    updater = Updater(settings.TELEGRAM_TOKEN, use_context=True)

    
    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = Bot(settings.TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    if settings.DEBUG:
        dp.bot.send_message(text='👋', chat_id=129013622)
    
    updater.start_polling()
    updater.idle()