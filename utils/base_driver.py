from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()


def create_driver():
    opts = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    return driver


def close_driver(driver):
    driver.close()


def open(driver, url):
    driver.get(url)
