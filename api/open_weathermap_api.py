from .base_api import BaseAPI
from utils.weather_class import WeatherData
import os


class OpenWeatherMapAPI(BaseAPI):
    try:
        AppID = os.environ['OWM_API_KEY']
    except KeyError:
        print('API_KEY environment variable does not exist')

    UNITS = {
        "metric": "°Celsius",
        "imperial": "°Fahrenheit"
    }

    def __init__(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        super().__init__(base_url)

    def get_temp(self, location, unit="metric"):
        result = self.get_request(f'?APPID={self.AppID}&q={location}&units={unit}').json()
        temp = result['main']['temp']
        unit = self.UNITS[unit]
        return WeatherData(temp, unit)
