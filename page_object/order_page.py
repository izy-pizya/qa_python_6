import allure

from XPATH import TestLocators
from page_object.base_page import *


class OrderPage(BasePage):
    order_url = 'https://qa-scooter.praktikum-services.ru/order'

    @allure.step("Инициализация драйвера")
    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.order_url

    @allure.step("Переход по ссылке")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("Заполнение поля Имя")
    def name_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.name_space).send_keys('Аллах')

    @allure.step("Заполнение поля Фамилия")
    def second_name_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.second_name_space).send_keys('Велик')

    @allure.step("Поле адрес")
    def address_field(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.address).send_keys('Пушкина')

    @allure.step("Поле со станцией метро")
    def add_metro_station(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.metro_station).click()
        page.finder(TestLocators.metro_station_active).click()

    @allure.step("Поле с номером телефона")
    def add_number(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.phone_number).send_keys('899991328129')
        page.finder(TestLocators.confirm_button).click()

    @allure.step("Выбор времени")
    def choose_time(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.order_time).click()
        page.finder(TestLocators.data_time).click()

    @allure.step("Количество дней аренды")
    def order_time(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.rent_duration).click()
        page.finder(TestLocators.five_days).click()

    @allure.step("Выбор цвета")
    def choose_color(self, locator):
        page = BasePage(self.driver)
        page.finder(locator).click()

    @allure.step("Поле комментарий")
    def add_comment(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.comment_for_delivery).send_keys('Тестовый комментарий')

    @allure.step("нажать на кнопку с доставкой")
    def click_to_deliver_button(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.deliver_button).click()

    @allure.step("Кнопка подтверждения")
    def click_to_confirm_order_button(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.confirm_order_button).click()

    @allure.step("Нажать на верхнюю кнопку заказа")
    def click_on_first_order_button(self):
        page = BasePage(self.driver)
        page.finder(TestLocators.order_button).click()

    @allure.step("Нажать на вторую кнопку заказа")
    def click_to_second_order_button(self):
        self.page = BasePage(self.driver)
        self.page.go_to_element(TestLocators.second_order_button)
        self.page.finder(TestLocators.second_order_button).click()

    @allure.step("Чравнения нужной ссылки")
    def assert_url(self):
        assert self.driver.current_url == self.order_url
