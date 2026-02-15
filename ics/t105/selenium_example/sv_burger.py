from selenium.webdriver.common.by import By

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://svburger1.co.il/#/SignUp")

fields = driver.find_elements(By.CLASS_NAME,"form-control")
fields[1].send_keys("dddsds")


base.selenium_end()
