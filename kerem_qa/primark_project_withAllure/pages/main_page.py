
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from kerem_qa.primark_project_withAllure.pages.locetors import MainPageLocators



class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def serach_for_item(self,item="Shoes"):
        self.driver.find_element(*MainPageLocators.SEARCH_FIELD).click()
        sale_button = self.wait.until(EC.visibility_of_element_located(*MainPageLocators.SEARCH_FIELD))

        search = self.driver.find_element(By.ID,"search-field").click()

        search.clear()
        search.send_keys(item)

    def click_button_and_get_text (self,text):
        button  = self.driver.find_element(By.PARTIAL_LINK_TEXT,text)
        button_text = button.text
        button.click()
        return button_text

    def click_on_cart_button(self):

            self.driver.find_element(By.ID,"shopping-bag-link").click()

    def get_and_verify_products_prices(self,price):
        pass






