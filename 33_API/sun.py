import requests
import datetime

parameters = {
    "lat": 48.631760,
    "lng":8.074650,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# JSON sunrise = 2023-03-05T17:18:19+00:00
# split T = ['2023-03-05', '06:00:08+00:00']
# split : = ['06', '00', '08+00', '00']

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)