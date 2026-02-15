import time
from time import sleep

from selenium.webdriver import Keys
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
search_menu = driver.find_element(By.ID,"gh-ac")
search_menu.click()
search_menu.clear()
search_menu.send_keys("Shirt")
search_menu.send_keys(Keys.RETURN)


driver.close()