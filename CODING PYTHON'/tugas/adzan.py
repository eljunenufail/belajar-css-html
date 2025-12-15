import requests
from tabulate import tabulate

kota = input("Masukkan nama kota: ")
target_url ="https://api.aladhan.com/v1/timingsByCity/13-12-2025?city=Jakarta&country=Indonesia&method=20"
# masukin data untuk kota yang diinput user
# penting!! mengubah hasil API menjadi dictionary Python dengan .json() biar bisa di proses
data = requests.get(target_url, params={
    "city": kota,
    "country": "Indonesia",
    "method": 20
}
).json()
if data["code"] == 200:
    waktu = data["data"]["timings"]
    tanggal = data["data"]["date"]["hijri"]["date"]
    table = [
        ["Imsak", waktu['Imsak']],
        ["Subuh", waktu['Fajr']],
        ["Dhuha", waktu['Dhuhr']],
        ["Zuhur", waktu['Dhuhr']],
        ["Ashar", waktu['Asr']],
        ["Magrib", waktu['Maghrib']],
        ["Isya", waktu['Isha']]
    ]

    # ada beberapa tampilan untuk table nya 1. fancy_grid (di tersambung tidak terputus putus) 2. grid (dia terputus putus) 
    # cara mengeluarkan table dengan "tablefmt="nama tampilan yang diinginkan"
    print(f"🏢 Nama kota: {kota}")
    print(f"Tanggal hijriyah: {tanggal}")
    print("-------------------------")
    print(tabulate
          (table, headers=["Sholat", "Waktu"], tablefmt="fancy_grid"))
    print("\n Terimakasih telah menggunakan program ini 😊")
















# import requests



# target_url ="https://api.aladhan.com/v1/timingsByCity/13-12-2025?city=Jakarta&country=Indonesia&method=20"
# response = requests.get(target_url)
# data = response.json()

# kota = (input("Masukkan nama kota: "))
# tanggal = data["data"]["date"]["hijri"]["date"]

# if data["code"] == 200:
#     jadwal = data["data"]["timings"]
#     print(f"🏢 nama kota: {kota}")
#     print(f"tanggal hijriyah: {tanggal}")
#     print("-------------------------")
#     print(f"Imsak: {jadwal['Imsak']}")
#     print(f"Subuh: {jadwal['Fajr']}")
#     print(f"Dhuha: {jadwal['Dhuhr']}")
#     print(f"Zuhur: {jadwal['Dhuhr']}")
#     print(f"Ashar: {jadwal['Asr']}")
#     print(f"Magrib: {jadwal['Maghrib']}")
#     print(f"Isya: {jadwal['Isha']}") 
