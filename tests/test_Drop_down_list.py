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
        element = page.finder(element_for_click)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(element_enabled)) > 0

    def test_how_much_does_it_cost(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.how_much_does_it_cost)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.how_much_does_it_cost_active)) > 0

    def test_several_scooters(self, click_to_first):
        page = BasePage(driver)
        element = page.finder(TestLocators.several_scooters)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.several_scooters_active)) > 0

    def test_how_is_it_calculated(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.how_is_it_calculated)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.how_is_it_calculated_active)) > 0

    def test_is_it_possible_to_order_a_scooter(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.is_it_possible_to_order_a_scooter)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.is_it_possible_to_order_a_scooter_active)) > 0

    def test_renew_your_subscription(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.renew_your_subscription)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.renew_your_subscription_active)) > 0

    def test_scooter_charger(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.scooter_charger)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.scooter_charger_active)) > 0

    def test_cancel_the_order(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.cancel_the_order)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.cancel_the_order_active)) > 0

    def test_distant_order(self, driver):
        page = BasePage(driver)
        element = page.finder(TestLocators.distant_order)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert len(page.finders(TestLocators.distant_order_active)) > 0