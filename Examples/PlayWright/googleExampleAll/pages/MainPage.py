from playwright.sync_api import expect


class MainPage:
    def __init__(self, page):
        self.__page = page
        self.__search_menu = page.locator("[name='q']")

    def search(self, pattern:str):
        expect(self.__search_menu).to_be_visible()
        self.__search_menu.click()
        self.__search_menu.fill(pattern)
        self.__search_menu.press("Enter")
