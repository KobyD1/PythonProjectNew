import unittest

from selenium.webdriver.common.by import By

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105


class SeleniumPytest(unittest.TestCase):


    def setUp(self):
        self.base=seleniumBase105()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")


    def tearDown(self):
        print('teat down')
        self.base.selenium_end()

    def test_login_by_css(self):
        user_name = self.driver.find_element(By.CSS_SELECTOR,"input[class*='input_error form_input']")
        user_name.send_keys("standard_user")
        password = self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']")
        password.send_keys("secret_sauce")

        print ("Test end")


    def test_login(self):
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        url=self.driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html","URL is not as expected after login "


