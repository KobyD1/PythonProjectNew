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

driver.get('https://www.zara.com/il/en/')
shopping_button = driver.find_element(By.PARTIAL_LINK_TEXT,"SHOPPING BAG")
text = shopping_button.text
print (text)
if ("[0]" in text):
    print ("0 found at shopping bag ")
else:
    print ("0 not found at shopping bag")


driver.close()
print ("Test End")
