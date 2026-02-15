from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class swag_labs4(BaseSelenium):
    base_selenium=BaseSelenium()
    driver = base_selenium.selenium_init("https://www.saucedemo.com/")

    user = driver.find_element(By.ID,'user-name')
    pw = driver.find_element(By.ID,'password')
    login = driver.find_element(By.ID,'login-button')

    user.click()
    user.clear()
    user.send_keys("standard_user")

    pw.click()
    pw.clear()
    pw.send_keys("secret_sauce")

    login_text = login.text
    print  ("login button text is ",login_text)
    login.submit()
    price=  driver.find_element(By.CLASS_NAME,'inventory_item_price')
    price.text
    print (price.text)
    prices= driver.find_elements_by_class_name('inventory_item_price')

    sleep(3)

    base_selenium.test_end()
    print ('test end')


