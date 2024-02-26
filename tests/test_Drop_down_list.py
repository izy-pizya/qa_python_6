import time

import allure
import pytest
from conftest import *
from page_object.main_page import *


#@allure.test('test')
class TestDropDownList():

    # Параметризированный тест (можно добавить еще переменных, дабы покрыть все пункты всплывающего окна)
    @pytest.mark.parametrize(
        "element_for_click, element_enabled",
        [
            (TestLocators.how_much_does_it_cost, TestLocators.how_much_does_it_cost_active),
            (TestLocators.several_scooters, TestLocators.several_scooters_active),
        ]
    )
    def test_all_test_in_one(self, driver, element_for_click, element_enabled):
        click_to_second_item = MainPage(driver)

        click_to_second_item.go_to_site()
        click_to_second_item.go_down(element_for_click)
        click_to_second_item.click_to_question(element_for_click)
        click_to_second_item.assert_text(element_enabled)

    def test_how_much_does_it_cost(self, driver):
        click_to_first_item = MainPage(driver)

        click_to_first_item.go_to_site()
        click_to_first_item.go_down(TestLocators.how_much_does_it_cost)
        click_to_first_item.click_to_question(TestLocators.how_much_does_it_cost)
        click_to_first_item.assert_text(TestLocators.how_much_does_it_cost_active)

    def test_several_scooters(self, driver):
        click_to_second_item = MainPage(driver)

        click_to_second_item.go_to_site()
        click_to_second_item.go_down(TestLocators.several_scooters)
        click_to_second_item.click_to_question(TestLocators.several_scooters)
        click_to_second_item.assert_text(TestLocators.several_scooters_active)

    def test_how_is_it_calculated(self, driver):
        click_to_third_item = MainPage(driver)

        click_to_third_item.go_to_site()
        click_to_third_item.go_down(TestLocators.how_is_it_calculated)
        click_to_third_item.click_to_question(TestLocators.how_is_it_calculated)
        click_to_third_item.go_down(TestLocators.how_is_it_calculated)
        click_to_third_item.assert_text(TestLocators.how_is_it_calculated_active)

    def test_is_it_possible_to_order_a_scooter(self, driver):
        click_to_fourth_item = MainPage(driver)

        click_to_fourth_item.go_to_site()
        click_to_fourth_item.go_down(TestLocators.is_it_possible_to_order_a_scooter)
        click_to_fourth_item.click_to_question(TestLocators.is_it_possible_to_order_a_scooter)
        click_to_fourth_item.assert_text(TestLocators.is_it_possible_to_order_a_scooter_active)

    def test_renew_your_subscription(self, driver):
        click_to_fifth_item = MainPage(driver)

        click_to_fifth_item.go_to_site()
        click_to_fifth_item.go_down(TestLocators.renew_your_subscription)
        click_to_fifth_item.click_to_question(TestLocators.renew_your_subscription)
        click_to_fifth_item.assert_text(TestLocators.renew_your_subscription_active)

    def test_scooter_charger(self, driver):
        click_to_sixth_item = MainPage(driver)

        click_to_sixth_item.go_to_site()
        click_to_sixth_item.go_down(TestLocators.scooter_charger)
        click_to_sixth_item.click_to_question(TestLocators.scooter_charger)
        click_to_sixth_item.assert_text(TestLocators.scooter_charger_active)

    def test_cancel_the_order(self, driver):
        click_to_seventh_item = MainPage(driver)

        click_to_seventh_item.go_to_site()
        click_to_seventh_item.go_down(TestLocators.cancel_the_order)
        click_to_seventh_item.click_to_question(TestLocators.cancel_the_order)
        click_to_seventh_item.assert_text(TestLocators.cancel_the_order_active)

    def test_distant_order(self, driver):
        click_to_eighth_item = MainPage(driver)

        click_to_eighth_item.go_to_site()
        click_to_eighth_item.go_down(TestLocators.distant_order)
        click_to_eighth_item.click_to_question(TestLocators.distant_order)
        click_to_eighth_item.assert_text(TestLocators.distant_order_active)
