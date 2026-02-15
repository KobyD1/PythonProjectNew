from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Selenium\Drivers\Chrome103\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome(executable_path="C:\Selenium\Drivers\Chrome103\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.com/")
input = driver.find_element(By.NAME,'q')

#
input.clear()
input.send_keys("python")
input.send_keys(Keys.ENTER)


sleep(3)
driver.close()
print ('noPom End')