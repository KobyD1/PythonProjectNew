from selenium.webdriver import Keys

from Examples.PythonCharm.Python.Selenium.googleall.GogglePages.locators import MainPageLocators


class GoogleMain():


    def __init__(self, driver):
        self.driver = driver
        print ('into init')

    def demo(self):
        print ('into outputs at google main')

    def searchForPattern(self,pattern):
        print ('into search for pattern')
        search = self.driver.find_element(*MainPageLocators.SEARCH)
        search.click()
        search.clear()
        search.send_keys(pattern)
        search.send_keys(Keys.ENTER)




    def search_for_pattern_updated(self,pattern):
        try:
            search = self.driver.find_element(*MainPageLocators.SEARCH)
            search.click
            search.send_keys(pattern)
            search.send_keys(Keys.ENTER)

        except:
            print ('exeption found')


        finally:
            print ('into finally')
