from XPATH import TestLocators
from page_object.base_page import *


class Order_page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/order"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def name_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.order_button).click()
        page.finder(TestLocators.name_space).send_keys('Аллах')

    def second_name_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.second_name_space).send_keys('Велик')

    def address_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.address).send_keys('Пушкина')

    def add_metro_station(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.metro_station).click()
        page.finder(TestLocators.metro_station_active).click()

    def add_number(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.phone_number).send_keys('899991328129')
        page.finder(TestLocators.confirm_button).click()

    def choose_time(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.order_time).click()
        page.finder(TestLocators.data_time).click()

    def order_time(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.rent_duration).click()
        page.finder(TestLocators.five_days).click()

    def choose_color(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.scooter_colour).click()

    def add_comment(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.comment_for_delivery).send_keys('Тестовый комментарий')

    def click_to_deliver_button(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.deliver_button).click()

    def click_to_accept_button_on_second_page(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.accept_button_on_second_page).click()

    def click_to_confirm_order_button(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.confirm_order_button).click()

    def click_to_second_order_button(self):
        page = BasePage(self.driver)
        element = page.finder(TestLocators.second_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()