from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()

driver = base.selenium_start_with_url("https://www.primark.com/en-gb")
sale_button = WebDriverWait(driver, 20).until( EC.visibility_of_element_located((By.LINK_TEXT, "SALE")))
sale_text=sale_button.text

sale_button.click()
print (F"sale_text: {sale_text}")





base.selenium_stop()
