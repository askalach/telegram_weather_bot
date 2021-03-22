import requests
import json

from settings import OPEN_WEATHER_MAP_ID

def get_weather(lat, lon):
    res = -1
    url = 'http://api.openweathermap.org/data/2.5/weather'

    # api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}
    payload = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'appid': OPEN_WEATHER_MAP_ID,
        'lang': 'ru'
    }
    c = 0
    while c < 10:
        response = requests.get(url, params=payload)
        if response.status_code == 200:
            break
        else:
            c += 1
    if c == 10:
        print('Can`t connect to weather server')
    else:
        res = response.json()
    return res


if __name__ == "__main__":
    # test_point = 'Saint Petersburg'
    lat = 59.56962
    lon = 30.12463
    weather = get_weather(lat, lon)
    if weather != -1:
        for k, v in weather.items():
            print(f'{k}: {v}')
