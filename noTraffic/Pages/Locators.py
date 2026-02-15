from selenium.webdriver.common.by import By


class WelcomePageLocators(object):
    WELCOME_BUTTONS = (By.CSS_SELECTOR, 'span.mat-button-wrapper')


class CreateZonePageLocetors(object):
    NAME = (By.ID, 'mat-input-0')


class GetAllZonesPageLocetors(object):
    LINE_TEXT = (By.CSS_SELECTOR, 'div.mat-list-text')
    DELETE = (By.CSS_SELECTOR, 'button[class*=mat-focus-indicator]')
    LINE_CLICK = (By.CSS_SELECTOR,'div.zone-item')
