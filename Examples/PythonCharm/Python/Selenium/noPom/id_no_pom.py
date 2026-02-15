from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# create a new Firefox session
driver = webdriver.Chrome(executable_path="../driver/chromedriver102.exe")
#driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.demoblaze.com/")

next = driver.find_element_by_id("next2")
pattern = next.text
print ('next button pattern is ',pattern)
next.click()

driver.quit()
print ('test success')