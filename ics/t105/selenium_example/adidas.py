from selenium.webdriver.common.by import By

from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()

driver = base.selenium_start_with_url("https://www.adidas.com/us/giftcards")

fields = driver.find_elements(By.CLASS_NAME,"_card-teaser-heading-title_130ar_143")


base.selenium_end()
