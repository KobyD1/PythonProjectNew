from time import sleep

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Selenium\Drivers\Chrome104\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
user = driver.find_element_by_id('user-name')
pw = driver.find_element_by_id('password')
login = driver.find_element_by_id('login-button')

user.click()
user.clear()
user.send_keys("standard_user")

pw.click()
pw.clear()
pw.send_keys("secret_sauce")

login_text = login.text
print  ("login button text is ",login_text)
login.submit()
price_text = driver.find_element_by_class_name('inventory_item_price').text
print ('after login we  got price of ',price_text)
assert price_text=='$29.99','failure found '
sleep(3)


driver.close()
print ('test end')


