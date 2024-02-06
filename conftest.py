import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_experimental_option('excludeSwitches', ['enable-logging'])
    o.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=o)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.maximize_window()
    yield driver
    driver.quit()

