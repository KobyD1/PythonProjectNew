import time
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.saucedemo.com/')
user=driver.find_element(By.ID,"user-name")
password =driver.find_element(By.NAME,"password")
login_button  = driver.find_element(By.ID,"login-button")

user.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()


driver.close()



#
# pw = driver.find_element(By.ID,"password")
# login= driver.find_element(By.ID,"login-button")
# user.send_keys("standard_user")
# pw.send_keys("secret_sauce")
# login.click()
#
# time.sleep(10)
# driver.close()
# print ("Test end")