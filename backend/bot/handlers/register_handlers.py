
from .auth import start

def handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])