from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_FIELD = ( By.ID,"search-field")




class CartPageLocetors(object):
    CART_TEXT = (By.CSS_SELECTOR, "h4[data-testautomation-id='title']")