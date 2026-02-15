from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/‏‏Chrome104/chromedriver.exe")
#driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.google.com")
try:

    search=driver.find_element(By.NAME,'qqq')

except:
    print('exeption found')
    search=driver.find_element(By.NAME,'q')

finally:
    print('into finally')
    search.click()
    search.clear()
    search.send_keys("Cat")
    search.send_keys(Keys.ENTER)







driver.quit()
print ('Test end')