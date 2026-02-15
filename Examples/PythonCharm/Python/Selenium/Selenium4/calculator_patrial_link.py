from time import sleep

from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class newtours_link(BaseSelenium):


    base = BaseSelenium()
    driver = base.selenium_init("https://www.calculator.net/")


    math=driver.find_element(By.PARTIAL_LINK_TEXT,"Math")
    math.click()

    search_btn=driver.find_element(By.ID,'bluebtn')
    pattern=search_btn.text
    base.test_end()

    print('test success ')
