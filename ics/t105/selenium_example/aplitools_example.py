from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get(' https://demo.applitools.com/#')

user= driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
login_button  = driver.find_element(By.ID,"log-in")

user.send_keys("abc")
password.send_keys("fake")
login_button.click()

driver.close()