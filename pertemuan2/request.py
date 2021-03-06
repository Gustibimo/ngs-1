import requests

request = requests.get("https://api.quran.sutanlab.id/surah/1/1")

response = request.json()

ayat_data = response['data']['text']

print(ayat_data['transliteration']['en'])

# latin_text = ayat_data['transliteration']['en']

# name = {'firstName': 'gusti', 'lastName': 'bimo'}

# print(name['firstName'])
# print(latin_text)