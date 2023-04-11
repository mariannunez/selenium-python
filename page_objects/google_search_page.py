from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.weather_class import WeatherData


class GoogleSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_element_text(self, by, locator):
        element = self.find_element_by(by, locator)
        return element.text

    def get_attribute_value(self, by, locator, attr):
        element = self.find_element_by(by, locator)
        return element.get_attribute(attr)

    def search(self, value):
        self.enter_text(By.NAME, "q", value)
        self.click(By.CSS_SELECTOR, "[role='listbox'] li")

    def get_temp(self, expected_unit='°Celsius'):
        unit_button = "//div[@class='vk_bk wob-unit']/a[contains(@style,'display:')]"
        unit = self.get_attribute_value(By.XPATH, f'{unit_button}/span', "aria-label")
        if unit != expected_unit:
            self.force_click(By.XPATH, unit_button)
        unit = self.get_attribute_value(By.XPATH, f'{unit_button}/span', "aria-label")
        temp_value = "wob_ttm" if expected_unit == '°Fahrenheit' else "wob_tm"
        temp = self.get_element_text(By.ID, temp_value)
        return WeatherData(temp, unit)
