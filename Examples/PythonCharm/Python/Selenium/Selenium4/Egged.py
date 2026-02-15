import math

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class Egged(BaseSelenium):
    base=BaseSelenium()
    driver= base.selenium_init("https://www.britannica.com/")
    search = driver.find_element(By.NAME,"query")
    search.click()
    search.clear()
    search.send_keys("Messi")
    search.send_keys(Keys.ENTER)
    base.test_end()

