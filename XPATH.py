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

    # Order page

    order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')

    second_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')

    name_space = (By.XPATH, '//input[@placeholder="* Имя"]')

    second_name_space = (By.XPATH, '//input[@placeholder="* Фамилия"]')

    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    metro_station = (By.XPATH, '//input[@class="select-search__input"]')

    phone_number = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    confirm_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    metro_station_active = (By.XPATH, '//li[./button[./div[@class="Order_Text__2broi" and text()="Черкизовская"]]]')

    # Next page of order

    order_time = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains (@placeholder, "* Когда привезти самокат")]')

    data_time = (By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--029"]')

    rent_duration = (By.XPATH, '//div[@class="Dropdown-control"]')

    five_days = (By.XPATH, '//div[@class="Dropdown-option" and text()="пятеро суток"]')

    scooter_colour = (By.XPATH, '//label[@for="black"]')

    gray_color = (By.XPATH, '//label[@for="grey"]')

    comment_for_delivery = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains (@placeholder, "Комментарий для курьера")]')

    deliver_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')

    confirm_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')

    status_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]')
