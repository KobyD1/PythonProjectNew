import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class advDemoTest(unittest.TestCase):


    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_checkbox_example(self):
        adv = self.driver.find_element(By.PARTIAL_LINK_TEXT,"Advanced").click()
        adv.click()

        time.sleep(2)
        desc = self.driver.find_element(By.NAME,"LH_TitleDesc")
        self.base.click_and_assert_on_element(desc)



