def chesee_toping(pizza):
    print(pizza+" with chesee toping")


def reminder(current_time):
    subuh = "4:40"
    dzuhur = "12:30"
    ashar = "15:30"
    maghrib = "1830"
    isha = "19:50"

    if(current_time == subuh):
        return "Sudah masuk waktu sholat shubuh"
    elif(current_time == dzuhur):
        return "Sudah masuk waktu sholat dzuhur"
    elif(current_time == ashar):
        return "Sudah masuk waktu sholat ashar"
    elif(current_time == maghrib):
        return "Sudah masuk waktu sholat maghrib"
    elif(current_time == isha):
        return "Sudah masuk waktu sholat isha"
    else:
        return "Belum masuk waktu sholat"

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")
print(reminder(current_time))
    