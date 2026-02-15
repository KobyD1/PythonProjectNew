from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.Selenium4.BaseSeleniumCommon import BaseSeleniumCommon


class find_elements:
    base_selenium=BaseSeleniumCommon("https://www.saucedemo.com/")

    driver = base_selenium.selenium_init()

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
    prices = driver.find_elements(By.CLASS_NAME,'inventory_item_price')
    for price in prices:
        price_from_page= price.text
        print (price_from_page)

    driver.close()
