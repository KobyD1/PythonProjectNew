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
driver.get("https://demoqa.com/login")

user = driver.find_element(By.ID,"userName")
user.click()
user.send_keys("Koby")

password = driver.find_element(By.ID,"password")
password.click()
password.send_keys("sdsdsdsds")
driver.close()