from geopy.location import Location
import requests
from datetime import datetime, timezone

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
issLongitude = float(response.json()['iss_position']['longitude'])
issLatitude = float(response.json()['iss_position']['latitude'])
DUBLatitude = 53.349804
DUBLongitude = -6.260310
LocationISS = (issLatitude,issLongitude)
TimeNowDUB = int(datetime.now(timezone.utc).hour)
latlngISS = ','.join(str(e) for e in LocationISS)
parametersISS = {
    "key": "",
    "latlng": latlngISS
}

parametersDUB = {
    "lat": DUBLatitude,
    "lng": DUBLongitude,
    "formatted": 0
}

def where_is_iss ():
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',params=parametersISS)
    response.raise_for_status
    data = response.json()
    print ("The ISS is now over" , data['results'][0]['address_components'][0]['long_name'])

where_is_iss()

def is_night():
    response = requests.get('https://api.sunrise-sunset.org/json', params=parametersDUB)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
    sunset = data['results']['sunset'].split('T')[1].split(":")[0]
    isNight = False
    if TimeNowDUB >= int(sunset) or TimeNowDUB <=int(sunrise):
        print("It's night in Dublin")
        isNight = True
    else:
        print("It's day in Dublin")
        isNight = False
    return isNight

def is_iss_overhead():
    isISSOverhead = False
    if DUBLatitude - 5 <= issLatitude <= DUBLatitude + 5 and DUBLongitude - 5 <= issLongitude <= DUBLongitude + 5:
        isISSOverhead = True
        print('Go outside! You can see the ISS Station now.')
    else:
        isISSOverhead = False
        print('Sorry, :-( You cannot see the ISS station now.')
    return isISSOverhead

is_night()
is_iss_overhead()




