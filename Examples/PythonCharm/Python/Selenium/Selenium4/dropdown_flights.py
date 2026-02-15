from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Examples.PythonCharm.Python.Selenium.Selenium4.BaseSeleniumCommon import BaseSeleniumCommon

base_selenium = BaseSeleniumCommon()
driver = base_selenium.selenium_init("https://demo.guru99.com/test/newtours/reservation.php")
from_port=driver.find_element(By.NAME,"fromPort")
drop_down_from_port=Select(from_port)
# Select(driver.find_element(By.NAME,'fromPort'))  # in one row
drop_down_from_port.select_by_index(2)


base_selenium.test_end()