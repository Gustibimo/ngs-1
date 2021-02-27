import telebot
import time

# pip install pyTelegramBotAPI

bot_token="1612575383:AAE6jIp9sBerJwPvrCYfLBcHz_SF4QQZ92c"

bot = telebot.TeleBot(token=bot_token)

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
