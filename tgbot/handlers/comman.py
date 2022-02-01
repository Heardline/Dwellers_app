from telegram import Update, ParseMode
from telegram.ext import CallbackContext

def command_start(update: Update,context: CallbackContext) -> None:
    update.effective_chat.send_message("Оо привет!",parse_mode=ParseMode.HTML)
    return None 