from selenium.webdriver.common.by import By

from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()
driver .get ("https://www.calculator.net/")
pasword= driver.find_element(By.PARTIAL_LINK_TEXT,"Password")
pasword.click()

lower = driver.find_element(By.ID,"ilower")
lower.submit()





base.selenium_end()