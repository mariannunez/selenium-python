from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator))).click()

    def find_element_by(self, by, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(( by, locator)))
        return self.driver.find_element(by=by, value=locator)

    def find_elements_by(self, by, locator):
        return self.driver.find_elements(by=by, value=locator)

    def enter_text(self, by, locator, value):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator))).send_keys(value)
