from selenium.webdriver.common.by import By


class TestLocators:
    how_much_does_it_cost = (By.XPATH, '//div[@id="accordion__heading-0"]')

    how_much_does_it_cost_active = (By.XPATH, '//div[@id="accordion__heading-0" and contains(@aria-expanded, "true")]')

    several_scooters = (By.XPATH, '//div[@id="accordion__heading-1"]')

    several_scooters_active = (By.XPATH, '//div[@id="accordion__heading-1" and contains(@aria-expanded, "true")]')

    how_is_it_calculated = (By.XPATH, '//div[@id="accordion__heading-2"]')

    how_is_it_calculated_active = (By.XPATH, '//div[@id="accordion__heading-2" and contains(@aria-expanded, "true")]')

    is_it_possible_to_order_a_scooter = (By.XPATH, '//div[@id="accordion__heading-3"]')

    is_it_possible_to_order_a_scooter_active = (By.XPATH, '//div[@id="accordion__heading-3" and contains(@aria-expanded, "true")]')

    renew_your_subscription = (By.XPATH, '//div[@id="accordion__heading-4"]')

    renew_your_subscription_active = (By.XPATH, '//div[@id="accordion__heading-4" and contains(@aria-expanded, "true")]')

    scooter_charger = (By.XPATH, '//div[@id="accordion__heading-5"]')

    scooter_charger_active = (By.XPATH, '//div[@id="accordion__heading-5" and contains(@aria-expanded, "true")]')

    cancel_the_order = (By.XPATH, '//div[@id="accordion__heading-6"]')

    cancel_the_order_active = (By.XPATH, '//div[@id="accordion__heading-6" and contains(@aria-expanded, "true")]')

    distant_order = (By.XPATH, '//div[@id="accordion__heading-7"]')

    distant_order_active = (By.XPATH, '//div[@id="accordion__heading-7" and contains(@aria-expanded, "true")]')

    order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')

