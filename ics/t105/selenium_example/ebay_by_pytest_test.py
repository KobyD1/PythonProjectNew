import unittest

from selenium.webdriver.common.by import By

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105


class eBayPytest(unittest.TestCase):
    def setUp(self):
        self.base=seleniumBase105()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")


    def tearDown(self):
        print('teat down')
        self.base.selenium_end()

    def test_search_clickable(self):
        search_button  = self.driver.find_element(By.ID,"gh-search-btn")
        is_displayed = search_button.is_displayed()
        assert is_displayed == True,"Button did not displayed as expected"


    def test_advanced_button(self):
        print ("Into Advanced Button")
        self.driver.find_element(By.LINK_TEXT, "Advanced").click()
        exp_url = self.driver.current_url
        assert exp_url == "https://www.ebay.com/sch/ebayadvsearch","URL did not changed as expected after click on Adv. button"


    def test_keyword_at_advanced(self):
        print ("Into Keyword in Advanced ")
        self.driver.find_element(By.LINK_TEXT, "Advanced").click()
        keyword_button = self.driver.find_element(By.ID, "s0-1-19-4[0]-7[1]-_in_kw")

        assert keyword_button.is_displayed() == True,"Button did not displayed as expected"