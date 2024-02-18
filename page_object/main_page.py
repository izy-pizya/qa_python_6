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
        return

    def click_to_(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.several_scooters)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_third(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.how_is_it_calculated)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_fourth(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.is_it_possible_to_order_a_scooter)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_fifth(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.renew_your_subscription)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_sixth(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.scooter_charger)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_seventh(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.cancel_the_order)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return

    def click_to_eighth(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.distant_order)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return