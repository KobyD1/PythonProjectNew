import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class pytestBefore(unittest.TestCase):

    def setUp(self):
        base = BaseSelenium()
        driver = base.selenium_init("https://www.saucedemo.com/")

    def test1(self):
        base = BaseSelenium()

        driver = base.selenium_init("https://www.saucedemo.com/")

        search = driver.find_element(By.CSS_SELECTOR, 'files[class^="input_erro"]')

        search.click()
        search.clear()
        search.send_keys("dress")
        search.send_keys(Keys.ENTER)


    def test3(self):
        print ('into test3')



    def tearDown(self):
        print ('into tear down')


