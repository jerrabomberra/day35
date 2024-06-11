import requests
from ISO3166 import ISO3166
import datetime

# abloom is at 13.773648654025774, 100.54110921045502
# current_datetime = datetime.now().replace(microsecond=0)
OEM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
# OEM_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
# API_KEY: str = '8c928036410e6f5ffc2690b3c94b81b8'
API_KEY: str = '254a494a8dd57422fd86e80ff181c546'

dt = datetime.datetime.fromtimestamp(0).replace(microsecond=0)

weather_params = {
    "lat": 13.773648654025774,
    "lon": 100.54110921045502,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}



def print_weather():
    response = requests.get(OEM_endpoint, params=weather_params)
    # print(response.json())
    if response.status_code == 200:
        rain_codes =[]
        is_rain_forecast = 0
        data = response.json()
        city = data['city']['name']
        temp = data['list'][0]['main']['temp']
        feels_like = data['list'][0]['main']['feels_like']
        rain_codes.append(data['list'][0]['weather'][0]['id'])
        rain_codes.append(data['list'][1]['weather'][0]['id'])
        rain_codes.append(data['list'][2]['weather'][0]['id'])
        rain_codes.append(data['list'][3]['weather'][0]['id'])
        print(rain_codes)
        for i in range(3):
            val = rain_codes[i]
            if 500 <= val <= 531:
                is_rain_forecast += 1
        if is_rain_forecast > 0:
            likely_rain = True
        else:
            likely_rain = False
        print(is_rain_forecast)
        print(likely_rain)
        # desc = data['weather'][0]['description']
        # country_code = data['sys']['country']
        # country = ISO3166[country_code]
        # print(f'Weather report for: {dt}')
        # print(f'Country: {country}')
        # print(f'City location: {city}')
        # print(f'Rain code: {rain} code {rain_code}')
        # print(f'Temperature: {temp} C')
        # print(f'Feels like: {feels_like} C')
        # print(f'Description: {desc.capitalize()}')
    else:
        print('Error fetching weather data')


print_weather()
