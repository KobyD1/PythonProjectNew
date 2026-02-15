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

driver.get('https://www.calculator.net/')
bmi_calc= driver.find_element(By.LINK_TEXT,"BMI Calculator")
bmi_calc.click()

current_url = driver.current_url
print (f"Current URl is {current_url}")
health_button = driver.find_element(By.PARTIAL_LINK_TEXT,"FITNESS")
health_button.click()
health_url = driver.current_url
print (f"the URL at helth page is {health_url}")
driver.close()