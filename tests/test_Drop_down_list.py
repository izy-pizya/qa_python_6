import time

import allure
import pytest
from conftest import *
from page_object.main_page import *


#@allure.test('test')
class Test_drop_down_list:

    # Параметризированный тест (можно добавить еще переменных, дабы покрыть все пункты всплывающего окна)
    @pytest.mark.parametrize(
        "element_for_click, element_enabled",
        [
            (TestLocators.how_much_does_it_cost, TestLocators.how_much_does_it_cost_active),
            (TestLocators.several_scooters, TestLocators.several_scooters_active),
        ]
    )
    def test_all_test_in_one(self, driver, element_for_click, element_enabled):
        page = BasePage(driver)
        open = Main_page(driver)

        open.go_to_site()
        element = page.finder(element_for_click)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        page.wait(element_for_click)
        element.click()
        assert len(page.finders(element_enabled)) > 0

    def test_how_much_does_it_cost(self, driver):
        click_to_first_item = Main_page(driver)

        click_to_first_item.go_to_site()
        click_to_first_item.click_to_first()
        click_to_first_item.click_to_first_qestion()
        assert len(driver.find_elements(*TestLocators.how_much_does_it_cost_active)) > 0

    def test_several_scooters(self, driver):
        click_to_second_item = Main_page(driver)

        click_to_second_item.go_to_site()
        click_to_second_item.click_to_second()
        click_to_second_item.click_to_second_qestion()
        assert len(driver.find_elements(*TestLocators.several_scooters_active)) > 0

    def test_how_is_it_calculated(self, driver):
        click_to_third_item = Main_page(driver)

        click_to_third_item.go_to_site()
        click_to_third_item.click_to_third()
        click_to_third_item.click_to_third_qestion()
        assert len(driver.find_elements(*TestLocators.how_is_it_calculated_active)) > 0

    def test_is_it_possible_to_order_a_scooter(self, driver):
        click_to_fourth_item = Main_page(driver)

        click_to_fourth_item.go_to_site()
        click_to_fourth_item.click_to_fourth()
        click_to_fourth_item.click_to_fourth_qestion()
        assert len(driver.find_elements(*TestLocators.is_it_possible_to_order_a_scooter_active)) > 0

    def test_renew_your_subscription(self, driver):
        click_to_fifth_item = Main_page(driver)

        click_to_fifth_item.go_to_site()
        click_to_fifth_item.click_to_fifth()
        click_to_fifth_item.click_to_fifth_qestion()
        assert len(driver.find_elements(*TestLocators.renew_your_subscription_active)) > 0

    def test_scooter_charger(self, driver):
        click_to_sixth_item = Main_page(driver)

        click_to_sixth_item.go_to_site()
        click_to_sixth_item.click_to_sixth()
        click_to_sixth_item.click_to_sixth_qestion()
        assert len(driver.find_elements(*TestLocators.scooter_charger_active)) > 0

    def test_cancel_the_order(self, driver):
        click_to_seventh_item = Main_page(driver)

        click_to_seventh_item.go_to_site()
        click_to_seventh_item.click_to_seventh()
        click_to_seventh_item.click_to_seventh_qestion()
        assert len(driver.find_elements(*TestLocators.cancel_the_order_active)) > 0

    def test_distant_order(self, driver):
        click_to_eighth_item = Main_page(driver)

        click_to_eighth_item.go_to_site()
        click_to_eighth_item.click_to_eighth()
        click_to_eighth_item.click_to_eighth_qestion()
        assert len(driver.find_elements(*TestLocators.distant_order_active)) > 0
