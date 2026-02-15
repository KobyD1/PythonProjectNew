
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class seleniumBasePrimark():



    def selenium_start_with_url(self,url):
        print("**** Test start ****")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def selenium_stop(self):
        print("**** Test stop ****")
        self.driver.close()

