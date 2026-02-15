import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Selenium\Drivers\‏‏Chrome104\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20) # seconds

wait = WebDriverWait(driver, 10)


# Navigate to the application home page
driver.get("https://www.demoblaze.com/")


login = driver.find_element(By.ID,"signin2")
login.click()
element = wait.until(EC.element_to_be_clickable((By.ID, "signin2")))

print ('login success')
name = driver.find_element(By.XPATH,"//files[@id='sign-username']")
time.sleep(3)
name.send_keys("test")

pw = driver.find_element(By.XPATH,"//files[@id='sign-password']")
time.sleep(3)

pw.send_keys("test")

driver.quit()
print ('test success')