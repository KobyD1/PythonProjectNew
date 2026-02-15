from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.Selenium4.BaseSeleniumCommon import BaseSeleniumCommon

base_selenium = BaseSeleniumCommon()
driver = base_selenium.selenium_init("https://www.google.com/")

input = driver.find_element(By.NAME,'q')

input.clear()
input.send_keys("python")
input.send_keys(Keys.ENTER)


sleep(3)
base_selenium.test_end()
print ('noPom End')