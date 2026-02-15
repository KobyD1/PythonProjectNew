import unittest

from selenium.webdriver.common.by import By

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105


class swagLabsTest(unittest.TestCase):
    def setUp(self):
        print ("into setup")
        self.base =seleniumBase105()
        self.driver =self.base.selenium_start_with_url("https://www.saucedemo.com/")



    def test_login_swag_labs(self):
        print ("into login")
        user= self.driver.find_element(By.ID,"user-name")
        password =self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html","URL is not as expected after login"



    def test_login_by_class(self):
        print ("into first_price")
        elements =self.driver.find_elements(By.CLASS_NAME,"input_error.form_input")
        user= elements[0]
        password = elements[1]
        user.send_keys("ffgfgf")
        password.send_keys("dfdfdfd")
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button.btn_action")
        login_button.click()


    def tearDown(self):
        print ("into teardown")


