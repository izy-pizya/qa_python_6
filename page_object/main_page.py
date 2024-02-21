from XPATH import TestLocators
from page_object.base_page import *


class Main_page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_to_first(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.how_much_does_it_cost)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_second(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.several_scooters)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_third(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.how_is_it_calculated)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_fourth(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.is_it_possible_to_order_a_scooter)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_fifth(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.renew_your_subscription)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_sixth(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.scooter_charger)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_seventh(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.cancel_the_order)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_to_eighth(self):
        page = BasePage(self.driver)
        webdriver_
        element = page.finder(TestLocators.distant_order)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
