import requests
from ISO3166 import ISO3166

# abloom is at 13.773648654025774, 100.54110921045502

API_KEY: str = '8c928036410e6f5ffc2690b3c94b81b8'
# lat: float = 13.7736
lat = 13.773648654025774
# long: float = 100.5411
long = 100.54110921045502
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric'

response = requests.get(URL)


def print_weather():
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        desc = data['weather'][0]['description']
        country_code = data['sys']['country']
        country = ISO3166[country_code]
        print(f'Country: {country}')
        print(f'City location: {city}')
        print(f'Temperature: {temp} C')
        print(f'Feels like: {feels_like} C')
        print(f'Description: {desc}')
    else:
        print('Error fetching weather data')


print_weather()
