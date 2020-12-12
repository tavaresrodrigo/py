import requests
from datetime import datetime, timezone

response = requests.get(url='http://api.open-notify.org/iss-now.json')
issLongitude = float(response.json()['iss_position']['longitude'])
issLatitude = float(response.json()['iss_position']['latitude'])
DUBLatitude = 53.349804
DUBLongitude = -6.260310
TimeNowDUB = int(datetime.now(timezone.utc).hour)

parametersDUB = {
    "lat": DUBLatitude,
    "lng": DUBLongitude,
    "formatted": 0
}

def is_night():
    response = requests.get('https://api.sunrise-sunset.org/json', params=parametersDUB)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
    sunset = data['results']['sunset'].split('T')[1].split(":")[0]
    isNight = False
    if TimeNowDUB >= int(sunrise) and TimeNowDUB <=int(sunrise):
        print("It's night")
        isNight = True
    else:
        print("It's day")
        isNight = False
    return isNight

def where_is_iss():
    print(issLatitude, issLongitude)
    
def is_iss_overhead():
    isISSOverhead = False
    if DUBLatitude - 5 <= issLatitude <= DUBLatitude + 5 and DUBLongitude - 5 <= issLongitude <= DUBLongitude + 5:
        isISSOverhead = True
    else:
        isISSOverhead = False
        where_is_iss()
    return isISSOverhead

is_night()
is_iss_overhead()




