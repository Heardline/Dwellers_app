import telebot
from dwellers.settings import TELEGRAM_BOT_TOKEN
from authentication.models import CustomUser

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Введите ваш временный код для привязки аккаунта:")


## Временная функция для тестирования авторизации
@bot.message_handler(func=lambda message: True)
def process_temp_code(message):
    temp_code = message.text
    try:
        user = CustomUser.objects.get(temp_code=temp_code)
        user.telegram_id = message.from_user.id
        user.temp_code = None
        user.save()
        bot.reply_to(message, "Ваш аккаунт успешно привязан!")
    except CustomUser.DoesNotExist:
        bot.reply_to(message, "Неверный временный код. Пожалуйста, попробуйте еще раз.")

bot.polling(none_stop=True)