import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture()
def create_driver(request):
    opts = Options()

    if os.environ.get('CI_EXECUTION', False):
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
    opts.page_load_strategy = 'normal'
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    request.cls.driver = webdriver.Chrome(service=chrome_service, options=opts)
    request.cls.driver.maximize_window()


def close_driver(driver):
    driver.close()


def open(driver, url):
    driver.get(url)
