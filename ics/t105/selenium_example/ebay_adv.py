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

driver.get('https://www.ebay.com/')

advanced_button = driver.find_element(By.LINK_TEXT,"Advanced")
adv_text = advanced_button.text
print (f"the text at Advanced button is {adv_text}")
advanced_button.click()

print (f"URL is {driver.current_url}")
driver.close()