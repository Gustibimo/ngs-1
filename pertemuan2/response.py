from datetime import datetime

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
    
    if user_message in ("jam berapa?", "jam berapa"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    else:
        return "Afwan, saya tidak mengerti"

import random

def greet():
    sentence = ["Halo, ada yg bisa saya bantu", "Selamat datang", 
    "Pagi Kak, apa kabar?","Assalamualaikum Kak", "Hola, amigos" ]
    r = random.randint(0,len(sentence)-1)
    return sentence[r]