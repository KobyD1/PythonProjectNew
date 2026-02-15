from time import sleep

from selenium.webdriver.common.by import By

from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium

base = BaseSelenium()
driver = base.selenium_init("https://demoqa.com/books")
search  = driver.find_element(By.ID,'searchBox')
search.click()
search.clear()
search.send_keys("GIT")

results = driver.find_elements(By.CLASS_NAME,"rt-td")
for result in results:
    print (result.text)

previous = driver.find_element(By.CSS_SELECTOR,"div[class=-previous]")
previous.text

previous_xpath = driver.find_element(By.XPATH,"//div[@class='-previous']")
print(previous_xpath.text)
base.test_end()

