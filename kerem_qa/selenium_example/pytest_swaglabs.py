import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class pytest_swaglabs(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")
    def tearDown(self):
        self.base.selenium_stop()

    def test_login_correct_details(self):
        print("Into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        time.sleep(3)   # example of delay
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html","URL did not chnged after login success "


    def test_drop_down_exampe(self):
        print("Into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        sort = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_as_drop_down = Select(sort)
        # sort_as_drop_down.select_by_visible_text("Price (low to high)")
        sort_as_drop_down.select_by_index(3)
        print ("ffgf")


    def test_css_example(self):
        print("Into test login")
        user = self.driver.find_element(By.CSS_SELECTOR, "input[class='input_error form_input']")
        user.send_keys("standard_user")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']")
        login_button.click()
        print ("trest end ")

