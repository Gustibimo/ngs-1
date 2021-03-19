import requests
import time
import telebot

# from getcontent import get_surah, get_tafsir
from surahlist import generate_surah_list
from response import bot_response, sample_response

# def get_ayat(nomor_surah, nomor_ayat):
#     url = "https://api.quran.sutanlab.id/surah/{surah_no}/{ayat_no}"
#     req = requests.get(url.format(surah_no=nomor_surah, ayat_no=nomor_ayat))
#     response = req.json()
#     ayat_arab = response["data"]["text"]["arab"]
#     return ayat_arab

# print(get_surah(1))

bot_token="1677750958:AAGkyaMLP5_nBnv1MOJYCbqkMInxd1R3rZ0"
bot = telebot.TeleBot(token=bot_token)


# # bot.send_message(181179145, "hai")
surah_list= generate_surah_list()

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '\U0001F64F Bismillah.. Berikut layanan yg dapat digunakan:\n\n \U0001F50D *Cari Surah* _ketik surah [spasi] nomor surat_\n\n \U0001F50D *Tampilkan tafsir surah* _ketik tafsir [spasi] nomor surat_',
     parse_mode='Markdown')   

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Assalamualaikum Akhi\n_Untuk menampilkan, ketik: surah [spasi] no/namasurat_\n*Menampilkan Surah dalam AlQuran:*', parse_mode='Markdown')
    bot.send_message(message.chat.id, surah_list) 
    bot.send_message(message.chat.id, '-- _Untuk menampilkan, ketik: surah [spasi] Nomor/Namasurat_ --', parse_mode='Markdown')

@bot.message_handler(func=bot_response)
def halo(message):
    bot.send_message(message.chat.id, bot_response(message), parse_mode='Markdown')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)