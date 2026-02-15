from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# create a new Firefox session
driver = webdriver.Chrome(executable_path="../driver/chromedriver100.exe")
driver.maximize_window()

driver.get("https://www.calculator.net/math-calculator.html")

button = driver.find_element_by_class_name("topNavOn")
pattern =button.text
link1= driver.find_element_by_link_text("Financial")
link1.click()
driver.get("https://www.calculator.net/math-calculator.html")

link2=driver.find_element_by_partial_link_text("Fina")
link2.click()


driver.quit()
print('test success ')
