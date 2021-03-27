import requests
import time
import telebot

from surahlist import generate_surah_list
from getcontent import get_surah, get_an

bot_token="token here"
bot = telebot.TeleBot(token=bot_token)

def bot_response(msg):
    input_text = msg.text
    user_message = str(input_text).lower()
    query = user_message.split(" ")
    
    command = query[0]
    nomor_ayat = query[1]

    if command in ("surah"):
        return get_surah(nomor_ayat)
    if command in ("an"):
        return get_an(nomor_ayat)
    else:
        return "Afwan"

surah_list= generate_surah_list()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Assalamualaikum Akhi\n_Untuk menampilkan, ketik: surah [spasi] no/namasurat_\n*Menampilkan Surah dalam AlQuran:*', parse_mode='Markdown')
    bot.send_message(message.chat.id, surah_list) 
    bot.send_message(message.chat.id, '-- _Untuk menampilkan, ketik: surah [spasi] Nomor/Namasurat_ --', parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '\U0001F64F Bismillah.. Berikut layanan yg dapat digunakan:\n\n \U0001F50D *Cari Surah* _ketik surah [spasi] nomor surat_\n\n \U0001F50D *Tampilkan tafsir surah* _ketik tafsir [spasi] nomor surat_',
     parse_mode='Markdown')  

@bot.message_handler(func=bot_response)
def halo(message):
    bot.send_message(message.chat.id, bot_response(message), parse_mode='Markdown')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
