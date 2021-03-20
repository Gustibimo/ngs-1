def generate_surah_list():
    f = open("/home/gbimo/workspace/telegrambot/pertemuan4/surat_latin.txt", "r")
    d =[]

    for i in f.readlines():
        d.append(i.rstrip("\n"))

    return "\n".join(str(number)+" "+letter for number, letter in enumerate(d,1))

def surah_map(nama_surat):
    f = open("/home/gbimo/workspace/telegrambot/pertemuan4/surat_latin.txt", "r")
    d =[]
    surah_map ={}
    nama_surat = nama_surat.lower()

    for i in f.readlines():
        d.append(i.rstrip("\n").lower())
    
    for nomor, surah in enumerate(d,1):
        surah_map[surah] = nomor

    return surah_map[nama_surat]

print(surah_map("al fatihah"))