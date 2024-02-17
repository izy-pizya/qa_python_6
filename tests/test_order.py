import time

import allure
import pytest
from conftest import *
from XPATH import TestLocators
from page_object.base_page import *

class Test_order:
    def test_order_by_first_button(self, driver):
        page = BasePage(driver)
        page.finder(TestLocators.order_button).click()
        page.finder(TestLocators.name_space).send_keys('Измаил')
        page.finder(TestLocators.second_name_space).send_keys('Набиулин')
        page.finder(TestLocators.address).send_keys('Пушкина')
        page.finder(TestLocators.metro_station).click()
        page.finder(TestLocators.metro_station_active).click()
        page.finder(TestLocators.phone_number).send_keys('899991328129')
        page.finder(TestLocators.confirm_button).click()
        # Next order page
        page.finder(TestLocators.order_time).click()
        page.finder(TestLocators.data_time).click()
        page.finder(TestLocators.rent_duration).click()
        page.finder(TestLocators.five_days).click()
        page.finder(TestLocators.scooter_colour).click()
        page.finder(TestLocators.comment_for_delivery).send_keys('Тестовый комментарий')
        page.finder(TestLocators.deliver_button).click()
        page.finder(TestLocators.accept_button_on_second_page).click()
        page.finder(TestLocators.confirm_order_button).click()
        #assert а хз что тут должно быть, сайт дальше не пускает

    def test_second_order_by_first_button(self, driver):
        page = BasePage(driver)
        page.finder(TestLocators.second_order_button).click()
        page.finder(TestLocators.name_space).send_keys('Измаил')
        page.finder(TestLocators.second_name_space).send_keys('Набиулин')
        page.finder(TestLocators.address).send_keys('Пушкина')
        page.finder(TestLocators.metro_station).click()
        page.finder(TestLocators.metro_station_active).click()
        page.finder(TestLocators.phone_number).send_keys('899991328129')
        page.finder(TestLocators.confirm_button).click()
        # Next order page
        page.finder(TestLocators.order_time).click()
        page.finder(TestLocators.data_time).click()
        page.finder(TestLocators.rent_duration).click()
        page.finder(TestLocators.five_days).click()
        page.finder(TestLocators.scooter_colour).click()
        page.finder(TestLocators.comment_for_delivery).send_keys('Тестовый комментарий')
        page.finder(TestLocators.deliver_button).click()
        page.finder(TestLocators.accept_button_on_second_page).click()
        page.finder(TestLocators.confirm_order_button).click()
        #assert а хз что тут должно быть, сайт дальше не пускает