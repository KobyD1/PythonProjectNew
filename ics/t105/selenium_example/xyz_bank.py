from selenium.webdriver.common.by import By

from t105.selenium_example.selenium_base_105 import seleniumBase105

base = seleniumBase105()
driver = base.selenium_start_with_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
buttons= driver.find_elements(By.CLASS_NAME,"btn.btn-primary.btn-lg")
buttons[1].click()
url =driver.current_url
print (url)
base.selenium_end()