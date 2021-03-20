from getcontent import get_surah, get_asbabun_nuzul

def bot_response(msg):
    input_text = msg.text
    user_message = str(input_text).lower()
    query = user_message.split(" ")
    
    command = query[0]
    nomor_ayat = query[1]

    if command in ("surah"):
        return get_surah(nomor_ayat)
    if command in ("asbabun-nuzul"):
        return get_asbabun_nuzul(nomor_ayat)
    else:
        return "Afwan"


def sample_response(msg):
    input_text = msg.text
    user_message = str(input_text).lower()

    if user_message in ("halo", "hi", "apa kabar"):
        return get_surah(3)
    
    if user_message in ("assalamualaikum"):
        return "Wa alamualaikum salam Kak, apa kabar?"
    
    if user_message in ("baik", "sehat", "alhamdulillah"):
        return "Alhamdulillah :)"
    
    if user_message in ("kamu siapa?", "kamu siapa?"):
        return "Saya Bot sholih yg siap bantu kamu"
    else:
        return "Afwan, saya tidak mengerti"
