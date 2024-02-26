from XPATH import TestLocators
from page_object.base_page import *


class MainPage(BasePage):

    main_url = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.main_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_down(self, locator):
        page = BasePage(self.driver)
        page.go_to_element(locator)

    def click_to_question(self, locator):
        page = BasePage(self.driver)
        page.finder(locator).click()

    def assert_text(self, locator):
        assert len(self.driver.find_elements(*locator)) > 0
