from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def finder(self, args):
        return self.driver.find_element(*args)

    def finders(self, args):
        return self.driver.find_elements(*args)
