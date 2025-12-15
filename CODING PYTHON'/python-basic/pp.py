import requests

def get_prayer_times(city):
    url = "https://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country": "Indonesia",
        "method": 20
    }

    response = requests.get(url, params=params)
    data = response.json()

    timings = data["data"]["timings"]
    hijri_date = data["data"]["date"]["hijri"]["date"]

    print(f"\n📍 Kota: {city}")
    print(f"📅 Tanggal Hijriah: {hijri_date}")
    print("--------------------------")
    print(f"Subuh    : {timings['Fajr']}")
    print(f"Dzuhur   : {timings['Dhuhr']}")
    print(f"Ashar    : {timings['Asr']}")
    print(f"Maghrib  : {timings['Maghrib']}")
    print(f"Isya     : {timings['Isha']}")

# Input dari user
city_name = input("Masukkan nama kota: ")
get_prayer_times(city_name)
