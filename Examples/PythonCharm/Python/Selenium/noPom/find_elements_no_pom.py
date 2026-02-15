from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# create a new Firefox session
from selenium.webdriver.common.service import Service

service = Service(executable_path="C:\Selenium\Drivers\Chrome103\chromedriver.exe")
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.demoblaze.com/")
categories = driver.find_element(By.CLASS_NAME,"list-group-item")
for cat in categories:
    pattern = cat.text
    print ('pattern found =',pattern)
    if pattern =='Phones':

        print ('phone found ')

driver.quit()