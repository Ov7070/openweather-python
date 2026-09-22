import requests as r

KEY = input("YOUR_API_KEY")
CITY = input("Enter city")

adr = "https://api.openweathermap.org/data/2.5/weather"

p = {
    "q": CITY,
    "appid": KEY,
    "units": "metric"
}

answer = r.get(adr, params=p)

print(answer.status_code)
print(answer.json())