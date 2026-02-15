from selenium.webdriver.common.by import By
#
# from ics.t105.selenium_example.selenium_base_105 import seleniumBase105
from ics.t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://svburger1.co.il/#/SignUp")
element = driver.find_element(By.CLASS_NAME,"form-control")
element.clear()
element.send_keys("Brenda")




base.selenium_end()