import telebot
import time
from nltk.chat.eliza import eliza_chatbot
from botdauroh import greet

# pip install pyTelegramBotAPI

bot_token="1677750958:AAGkyaMLP5_nBnv1MOJYCbqkMInxd1R3rZ0"

bot = telebot.TeleBot(token=bot_token)

user = bot.get_me()

@bot.message_handler(func=lambda msg: msg.text is not None)
def halo(message):
    bot.send_message(181179145, eliza_chatbot.respond('message'))

@bot.message_handler(func=lambda msg: msg.text is not None)
def halo(message):
    bot.send_message(181179145, greet())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "selamat datang") 


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "masukan username kamu")



#@bot.message_handler(func=lambda msg: if '@' is )

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
