import unittest

import allure

from kerem_qa.primark_project_withAllure.globals import BASE_URL, MAX_PRICE
from kerem_qa.primark_project_withAllure.pages.cart_page import CartPage
from kerem_qa.primark_project_withAllure.pages.main_page import MainPage
from kerem_qa.primark_project_withAllure.tests.selenium_base_primark import seleniumBasePrimark


class allTests(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBasePrimark()
        self.driver = self.base.selenium_start_with_url(BASE_URL)
        self.main_page = MainPage(self.driver)
        self.cart_page= CartPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    @allure.title("Login Test")
    @allure.description("Verify that a user can log in successfully.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        assert True

    def test_demo(self):
        assert True
    def test_click_on_gift_card_button(self):
        button_text = self.main_page.click_button_and_get_text("Gift")
        assert button_text == "Gift Card","Gift card button text is not as expected"

    def test_click_on_cart_button(self):
        with allure.step("Click on cart button"):

            self.main_page.click_on_cart_button()
            self.cart_page.get_cart_message()

    def test_find_product(self):
        with allure.step("Find product"):

            self.main_page.serach_for_item("Shirt")

    def test_get_item_prices(self):
        self.main_page.get_and_verify_products_prices(MAX_PRICE)



