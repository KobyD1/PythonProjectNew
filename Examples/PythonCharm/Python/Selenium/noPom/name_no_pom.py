import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="../driver/chromedriver100.exe")
driver.maximize_window()

driver.get("https://www.guru99.com/live-selenium-project.html")
time.sleep(3)
email = driver.find_element_by_id("awf_field-93653884")
email.click()
email.send_keys("test@outputs.com")
submit = driver.find_element_by_name("submit")

submit.click()

driver.quit()
print ('test success')