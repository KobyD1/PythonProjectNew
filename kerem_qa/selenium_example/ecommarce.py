from selenium.webdriver.common.by import By

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
# driver = base.selenium_start()
#
# driver.get("https://www.nike.com/il/")
driver = base.selenium_start_with_url("https://ecommerce-playground.lambdatest.io")
icons = driver.find_elements(By.CLASS_NAME,"figure-img.img-fluid.lazy-load")
prices = driver.find_elements(By.CLASS_NAME,"price-new")
base.selenium_stop()
