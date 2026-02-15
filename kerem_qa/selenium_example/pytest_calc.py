import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class advDemoTest(unittest.TestCase):


    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_checkbox_example(self):

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Grade").click()
        grade_1 = self.driver.find_element(By.NAME,"s1")
        grade_1.clear()
        grade_1.send_keys("100")

        grade_2 = self.driver.find_element(By.NAME, "s2")
        grade_2.clear()
        grade_2.send_keys("90")

        calc_button = self.driver.find_element(By.NAME,"x")
        calc_button.click()
        result = self.driver.find_element(By.CSS_SELECTOR,"p.verybigtext")
        text = result.text
        index_1 = text.index(":")+1
        index_2 = text.index("(")
        text = text[index_1:index_2].strip()
        text_as_float = float(text)
        assert text_as_float >= 90 , "the final grade is lower than 90"
        print (F"text found ={text}")




