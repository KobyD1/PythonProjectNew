from selenium.webdriver.common.by import By

from kerem_qa.primark_project_withAllure.pages.locetors import CartPageLocetors


class CartPage:
    def __init__(self,driver):
        self.driver = driver

    def get_cart_message(self):
        cart_text = self.driver.find_element(*CartPageLocetors.CART_TEXT).text
        print (cart_text)
        return cart_text