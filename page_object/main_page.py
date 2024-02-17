from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import TestLocators
from page_object.base_page import *


class Main_page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_to_first(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.how_much_does_it_cost)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()