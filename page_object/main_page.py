from XPATH import TestLocators
from page_object.base_page import *
import allure


class MainPage(BasePage):

    main_url = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.main_url

    @allure.step("Инициализация драйвера")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("спуститься вниз")
    def go_down(self, locator):
        page = BasePage(self.driver)
        page.go_to_element(locator)

    @allure.step("кликнуть на элемент к которому спускались")
    def click_to_question(self, locator):
        page = BasePage(self.driver)
        page.finder(locator).click()

    @allure.step("Проверка нужного вопроса")
    def assert_text(self, locator):
        assert len(self.driver.find_elements(*locator)) > 0
