name = "Gusti Bimo"


import random
def random_number():
    return random.randint(0,100)

# def cheese_toping(pizza):
#     return pizza + " with cheese toping"

def say_alhamdulillah(message):
    return message.split(" ")[1] + " baik, alhamdulillah"

def greet():
    sentence = ["halo, ada yg bisa saya bantu", "Selamat datang", 
    "Pagi Kak, apa kabar?","Assalamualaikum Kak", "Hola, amigos" ]
    r = random.randint(0,len(sentence)-1)
    return sentence[r]

import datetime
def remind(user_time):
    subuh = "04:40"
    dzuhur ="12:00"
    ashar = "15:30"
    maghrib = "18:30"
    isha = "19:50"

    if (user_time==subuh):
        return "Ayo sholat subuh"
    elif(user_time==dzuhur):
        return "Waktunya adzan dzuhur utk Jakarta dan sekitarnya"
    elif(user_time==ashar):
        return "Waktunya adzan ashar utk Jakarta dan sekitarnya"
    elif(user_time==maghrib):
        return "Waktunya adzan maghrib utk Jakarta dan sekitarnya"
    elif(user_time==isha):
        return "Waktunya adzan isha utk Jakarta dan sekitarnya"
    else:
        return "Belum masuk waktu sholat"


cheese_toping = lambda pizza:  f'{pizza} with cheese toping'