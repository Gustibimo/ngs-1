import requests

base_url = "https://api.quran.sutanlab.id/surah/"
req = requests.get(base_url)
response = req.json()

def get_surah(surah_id):
    surah = "https://api.quran.sutanlab.id/surah/{surah_no}"   
    req = requests.get(surah.format(surah_no=surah_id))
    response = req.json()
    verses = response["data"]["verses"]
    surah_name = response["data"]["name"]
    surah_name_id = "*Menampilkan Quran Surat* _"+surah_name["transliteration"]["id"]+":_"
    return surah_name_id+"\n\n"+"\n\n".join(verse["text"]["arab"]+"\n\n"+"_"+verse["translation"]["id"]+"_" for verse in verses[:10])

def get_asbabun_nuzul(surah_id):
    surah = "https://api.quran.sutanlab.id/surah/{surah_no}"   
    req = requests.get(surah.format(surah_no=surah_id))
    response = req.json()
    asbab = response["data"]["tafsir"]
    return asbab["id"]

from surahlist import surah_map
def get_asbabun_nuzul_surah(nama_surat):
    nama_surat = nama_surat.lower()
    surah_no=surah_map(nama_surat)
    surah = "https://api.quran.sutanlab.id/surah/{surah_no}"   
    req = requests.get(surah.format(surah_no=surah_no))
    response = req.json()
    asbab = response["data"]["tafsir"]
    return asbab["id"]