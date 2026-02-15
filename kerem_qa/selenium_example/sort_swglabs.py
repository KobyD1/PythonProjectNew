from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start_with_url("https://www.saucedemo.com/")
elements = driver.find_elements(By.CLASS_NAME,"input_error.form_input")
user = elements[0]
user.send_keys("standard_user")
password = elements[1]
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID,"login-button")
login_button.click()

sort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
sort.select_by_index(2)
sort.select_by_visible_text("Price (high to low)")

base.selenium_stop()