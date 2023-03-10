import requests
from datetime import datetime

parameters = {
    "lat": 48.631760,
    "lng": 8.074650,
    "formatted": 0,
}


def is_iss_overhead():
    # ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude =  float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    my_longitude = parameters["lng"]
    my_latitude = parameters["lat"]

    print(f"Position ISS longitude: {longitude} && laditude {latitude}.")
    print(f"My Position longitude: {my_longitude} && laditude {my_latitude}.")

    if my_latitude-5 <= latitude <= my_latitude+5 and my_longitude-5 <= longitude <= my_longitude+5:
        return True
    
def is_night():
    # daytime
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True

if is_night() and is_iss_overhead():
    print("Lookup!!!!!!")
else:
    print("Nothing to see.")
    
# if the ISS is close to my current position
# and t
# it is currently dark
# send me an email and tell me look up
# BONUS: run the code every 60 seconds. 