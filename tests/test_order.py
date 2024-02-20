import time
from conftest import *
from page_object.order_page import *
from page_object.main_page import *


class Test_order:
    def test_order_by_first_button(self, driver):
        order_page = Order_page(driver)

        order_page.go_to_site()
        order_page.name_field()
        order_page.second_name_field()
        order_page.address_field()
        order_page.add_metro_station()
        order_page.add_number()
        order_page.choose_time()
        order_page.order_time()
        order_page.choose_color()
        order_page.add_comment()
        order_page.click_to_deliver_button()
        order_page.click_to_accept_button_on_second_page()

        time.sleep(10)

        #assert а хз что тут должно быть, сайт дальше не пускает

    def test_second_order_by_first_button(self, driver):
        main_page = Main_page(driver)

        main_page.go_to_site()

        order_page = Order_page(driver)

        order_page.click_to_second_order_button()
        order_page.name_field()
        order_page.second_name_field()
        order_page.address_field()
        order_page.add_metro_station()
        order_page.add_number()
        order_page.choose_time()
        order_page.order_time()
        order_page.choose_color()
        order_page.add_comment()
        order_page.click_to_deliver_button()
        order_page.click_to_accept_button_on_second_page()

        #assert а хз что тут должно быть, сайт дальше не пускает