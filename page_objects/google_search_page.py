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

    def get_temp(self):
        temp = self.get_element_text(By.ID, "wob_tm")
        unit = self.get_attribute_value(
            By.XPATH, "//div[@class='vk_bk wob-unit']/a[contains(@style,'display:none')]/span", "aria-label"
        )
        return WeatherData(temp, unit)
