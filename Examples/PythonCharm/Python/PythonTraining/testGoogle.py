from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys


print ('start test')
driver = webdriver.Chrome('C:/Selenium/Drivers/Chrome102/chromedriver.exe')

driver.get("https://www.google.com")
print(driver.title)
elem = driver.find_element_by_id("files")
elem.clear()
elem.send_keys("Haifa")
elem.send_keys(Keys.RETURN)
time.sleep(10)
driver.close()
print ('*** end test ***')
