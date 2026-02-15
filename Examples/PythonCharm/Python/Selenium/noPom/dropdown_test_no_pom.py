import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="../driver/chromedriver100.exe")
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/")
time.sleep(3)

buttons = driver.find_elements_by_class_name("btn.btn-primary.btn-lg")
buttons[0].click()

select = Select(driver.find_element_by_id('userSelect'))

# select by visible text
select.select_by_visible_text('Harry Potter')

# select by value
select.select_by_value('1')
driver.quit()
print ('test success')