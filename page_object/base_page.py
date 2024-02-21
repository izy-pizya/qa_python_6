class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def finder(self, locator):
        return self.driver.find_element(*locator)

    def finders(self, locator):
        return self.driver.find_elements(*locator)
