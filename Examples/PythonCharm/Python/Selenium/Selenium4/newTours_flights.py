from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


class newTours_flights(BaseSelenium):
    base=BaseSelenium()
    driver = base.selenium_init("https://demo.guru99.com/selenium/newtours/reservation.php")

    from_port=driver.find_element(By.NAME,"fromPort")
    Select(from_port).select_by_index(2)
    Select(from_port).select_by_value("Paris")

    base.test_end()

