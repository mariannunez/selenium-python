from utils.base_driver import create_driver, close_driver, open
from page_objects.google_search_page import GoogleSearchPage
from api.open_weathermap_api import OpenWeatherMapAPI
import math


class TestClass:
    def test_weather_services(self):
        # create an driver instance
        driver = create_driver()

        # Go to the google page
        open(driver, 'https://www.google.com/')

        # Search weather in an specific location
        google_search_page = GoogleSearchPage(driver)
        google_search_page.search("Weather in San Francisco, California")

        # Search weather in an specific location by API
        google_temp = google_search_page.get_temp()
        open_weather_map = OpenWeatherMapAPI()
        open_weather_temp = open_weather_map.get_temp("San Francisco")

        # Print results
        print("Google temp: ", google_temp)
        print("Open Weathermap temp: ", open_weather_temp)
        temp_diff = float(google_temp.temp) - float(open_weather_temp.temp)
        print("Temperature difference: ", temp_diff)

        # Add assertion
        assert round(temp_diff) in range(-2, 2)

