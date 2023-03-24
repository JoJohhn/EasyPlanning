from django.core.management.base import BaseCommand
from telebot import TeleBot
from tgbotapp.TOKEN import TOKEN
from tgbotapp.logic import save_tg_user_ids


bot = TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, этот бот будет присылать уведомления, проверить работоспособность можно, что-нибудь написав")
    user_id = message.from_user.id
    user_name = message.from_user.username
    save_tg_user_ids(user_id, user_name)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    user_id = message.from_user.id
    user_name = message.from_user.username


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()