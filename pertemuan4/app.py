import requests
import time
import telebot

from getcontent import get_surah

bot_token="1677750958:AAGkyaMLP5_nBnv1MOJYCbqkMInxd1R3rZ0"
bot = telebot.TeleBot(token=bot_token)

def bot_response(msg):
    input_text = msg.text
    user_message = str(input_text).lower()
    query = user_message.split(" ")
    
    command = query[0]
    nomor_ayat = query[1]

    if command in ("surah"):
        return get_surah(nomor_ayat)
    else:
        return "Afwan"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello", parse_mode='Markdown')

@bot.message_handler(func=bot_response)
def halo(message):
    bot.send_message(message.chat.id, bot_response(message), parse_mode='Markdown')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
