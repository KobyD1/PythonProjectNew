from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.Selenium4.BaseSelenium import BaseSelenium


class newTours_regsiter(BaseSelenium):
    base=BaseSelenium()
    driver= base.selenium_init("https://demo.guru99.com/test/newtours/index.php")

    register=driver.find_element(By.LINK_TEXT,"REGISTER")
    register.click()

    first_name=driver.find_element(By.NAME,"firstName")
    base.input_to_element(first_name,"John")


    base.test_end()