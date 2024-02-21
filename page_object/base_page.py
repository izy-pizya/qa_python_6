from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def finder(self, locator):
        return self.driver.find_element(*locator)

    def finders(self, locator):
        return self.driver.find_elements(*locator)

    def wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
