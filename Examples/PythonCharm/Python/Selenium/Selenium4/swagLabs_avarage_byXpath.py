from time import sleep

from Examples.PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


class swagLabs_avarage_byXpath(BaseSelenium):

    base_selenium=BaseSelenium()
    driver = base_selenium.selenium_init("https://www.saucedemo.com/")
    sleep(3)


    base_selenium.login_to_swagLabs('standard_user','secret_sauce')
    base_selenium.find_price_by_xpath()
    base_selenium.test_end()
