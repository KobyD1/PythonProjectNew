from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GoogleMain(object):

    def __init__(self, driver):
        self.driver = driver
        print('into init')

    def demo(self):
        print('into outputs at google main')

    def searchForPattern(self, pattern):
        print('into search for pattern')
        try:
            search = self.driver.find_element(By.NAME, "q")
            search.click()
            search.clear()
            search.send_keys(pattern)
            search.send_keys(Keys.ENTER)
        except:
            print('exeption found')

        finally:
            print('into finally')
