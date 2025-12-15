import requests

target_url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
print(f"target url : {target_url}")
#HTTP GET (tarik data)
response = requests.get(target_url)
#konversi ke json
data = response.json()
print("reponse data:", data)

# mengambil data shubuh
jadwal = data["data"]["timings"]
shubuh = jadwal["Fajr"]
dzuhur = jadwal["Dhuhr"]
print(f"Waktu shubuh: {shubuh}")
print(f"Waktu dzuhur: {dzuhur}")

