from selenium.webdriver.common.by import By

from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()
driver .get ("https://www.ebay.com/")

driver.find_element(By.LINK_TEXT,"Advanced").click()
title_desc= driver.find_element(By.NAME,"LH_TitleDesc")
before =title_desc.is_selected()
print (f"the status before is {before}")
if (not before):
    title_desc.click()


after=title_desc.is_selected()
print (f"the status after is {after}")

base.selenium_end()