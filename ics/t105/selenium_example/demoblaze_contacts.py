from selenium.webdriver.common.by import By

from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start()
driver .get ("https://www.demoblaze.com/")

contact = driver.find_element(By.LINK_TEXT, "Contact")
contact_text = contact.text

if (contact_text=="Contact"):
    print ("Text found as expected ")
    contact.click()

else:
    print ("Text not found as expected ")

base.selenium_end()