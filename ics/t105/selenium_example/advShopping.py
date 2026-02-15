from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://advantageonlineshopping.com/#/")
# contact = driver.find_element(By.PARTIAL_LINK_TEXT, "CONTACT")
# contact.click()
category = driver.find_element(By.NAME,"categoryListboxContactUs")
select_as_drop_down= Select(category)
select_as_drop_down.select_by_index(1)




base.selenium_end()