import unittest
from selenium.webdriver.common.by import By
from ics.t105.selenium_example.selenium_base_105 import seleniumBase105


class swagLabsTest(unittest.TestCase):
    def setUp(self):
        print ("into setup")
        self.base =seleniumBase105()
        self.driver =self.base.selenium_start_with_url("https://www.saucedemo.com/")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")


        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "URL is not as expected after login"






    def test_first_price_swag_labs(self):
        print ("into first_price")
        first_price = self.driver.find_element(By.CLASS_NAME,"inventory_item_price")
        assert first_price.text =="$29.99"

    def tearDown(self):
        print ("into teardown")
        self.base.selenium_end()


