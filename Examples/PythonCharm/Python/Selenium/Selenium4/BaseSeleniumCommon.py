from time import sleep

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver



class BaseSeleniumCommon(object):
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.driver = driver


    def selenium_init(self,url):
        driver=self.driver
        driver.get(url)
        driver.maximize_window()
        sleep(3)
        return driver

    def login(self):
        driver=self.driver
        user = driver.find_element(By.ID, 'user-name')
        pw = driver.find_element(By.ID, 'password')
        login = driver.find_element(By.ID, 'login-button')

        user.click()
        user.clear()
        user.send_keys("standard_user")

        pw.click()
        pw.clear()
        pw.send_keys("secret_sauce")

        login_text = login.text
        print("login button text is ", login_text)
        login.submit()

    def test_end(self):
        print('The test Success')
        self.driver.close()

    def input_to_element(self,web_element, pattern):
        print ('Try to send keys to web element ')
        web_element.click()
        web_element.clear()
        web_element.send_keys(pattern)

    def test_login_to_swagLabs(self, user_text,pw_text):
        user_element = self.driver.find_element(By.ID, 'user-name')
        pw_element = self.driver.find_element(By.ID, 'password')
        #set user
        user_element.click()
        user_element.clear()
        user_element.send_keys(user_text)
        pw_element.click()
        pw_element.clear()
        pw_element.send_keys(pw_text)
        #click on submit
        login_button=self.driver.find_element(By.ID,'login-button')
        login_button.submit()


    def find_price_by_xpath(self):
        print ('try to find prices ')
        price=self.driver.find_element(By.XPATH,"//div[@class='inventory_item_price']")
        print("The price is ",price.text)

