from selenium.webdriver.common.by import By

from ics.t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://www.calculator.net/")

links = driver.find_elements(By.PARTIAL_LINK_TEXT,"Calculator")

for link in links:
    print (link.text)


base.selenium_end()