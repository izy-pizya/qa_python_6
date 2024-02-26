from XPATH import TestLocators
from page_object.base_page import *


class Main_page:

    main_url = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.main_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_down(self, locator):
        self.page = BasePage(self.driver)
        element = self.page.finder(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_to_question(self, locator):
        page = BasePage(self.driver)
        page.wait(locator)
        page.finder(locator).click()