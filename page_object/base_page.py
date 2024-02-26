from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def finder(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def finders(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_elements_located(locator),
                                                      message=f'Element not found in {locator}')

    def go_to_element(self, locator):
        self.page = BasePage(self.driver)
        element = self.page.finder(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
