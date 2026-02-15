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

driver.get('https://www.calculator.net/')
age_link = driver.find_element(By.LINK_TEXT,"Age Calculator")
age_link.click()

driver.find_element(By.PARTIAL_LINK_TEXT,"FITNESS").click()
text = driver.find_element(By.PARTIAL_LINK_TEXT,"FITNESS").text

if (text.__contains__("&")):
    print (F"Fitnees button define as expected the text is {text}")
# example how to get URL
url = driver.current_url
print(url)

if (url == 'https://www.calculator.net/fitness-and-health-calculator.html'):
    print ("Test OK -URL as expected")

else:
    print ("#####Test FAILED -URL not as expected######")

driver.close()