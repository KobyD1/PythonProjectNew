import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class advDemoTest(unittest.TestCase):


    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_dropdown_example(self):
        print ("start test for drop down example")
        time.sleep(3)
        contact_us = self.driver.find_element(By.PARTIAL_LINK_TEXT,"CONTACT")
        contact_us.click()

        category = self.driver.find_element(By.NAME,"categoryListboxContactUs")
        category_as_drop_down = Select(category)

        category_as_drop_down.select_by_visible_text("Mice")

        product  = Select(self.driver.find_element(By.NAME,"productListboxContactUs"))
        time.sleep(3)

        product.select_by_index(2)
        email = self.driver.find_element(By.NAME,"emailContactUs")
        email.send_keys("demo@gmail.com")
        subject = self.driver.find_element(By.NAME,"subjectTextareaContactUs")
        subject.send_keys("Hi please provide details")

        send = self.driver.find_element(By.ID,"send_btn")
        is_displayed = send.is_displayed()
        assert is_displayed == True , "Send button did not displayed as expected"


        print ("into test")

