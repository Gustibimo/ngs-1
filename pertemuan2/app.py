import telebot
import time

bot_token="1677750958:AAGkyaMLP5_nBnv1MOJYCbqkMInxd1R3rZ0"

bot = telebot.TeleBot(token=bot_token)

user = bot.get_me()

def sample_response(msg):
    input_text = msg.text
    user_message = str(input_text).lower()

    if user_message in ("halo", "hi", "apa kabar"):
        return "Assalamualaikum Kak, apa kabar?"
    
    if user_message in ("assalamualaikum"):
        return "Wa alamualaikum salam Kak, apa kabar?"
    
    if user_message in ("baik", "sehat", "alhamdulillah"):
        return "Alhamdulillah :)"
    
    if user_message in ("kamu siapa?", "kamu siapa?"):
        return "Saya Bot sholih yg siap bantu kamu"
    else:
        return "Afwan, saya tidak mengerti"
    
@bot.message_handler(func=sample_response)
def halo(message):
    bot.send_message(message.chat.id, sample_response(message))

# @bot.message_handler(func=lambda msg: msg.text is not None)
# def halo(message):
#     bot.send_message(181179145, eliza_chatbot.respond('message'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "selamat datang") 

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
