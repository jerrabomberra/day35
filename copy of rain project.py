# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

import requests
from ISO3166 import ISO3166
import datetime

# abloom is at 13.773648654025774, 100.54110921045502
# current_datetime = datetime.now().replace(microsecond=0)
OEM_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY: str = '8c928036410e6f5ffc2690b3c94b81b8'

dt = datetime.datetime.fromtimestamp(0).replace(microsecond=0)

weather_params = {
    "lat": 13.773648654025774,
    "lon": 100.54110921045502,
    "appid": API_KEY,
    "units": "metric",
}



def print_weather():
    response = requests.get(OEM_endpoint, params=weather_params)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        desc = data['weather'][0]['description']
        country_code = data['sys']['country']
        country = ISO3166[country_code]
        print(f'Weather report for: {dt}')
        print(f'Country: {country}')
        print(f'City location: {city}')
        print(f'Temperature: {temp} C')
        print(f'Feels like: {feels_like} C')
        print(f'Description: {desc.capitalize()}')
    else:
        print('Error fetching weather data')


print_weather()
