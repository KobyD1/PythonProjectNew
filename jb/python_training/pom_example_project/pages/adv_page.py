

class AdvPage:
    def __init__(self,page):
        self.page = page

    def search_for_item(self,item):
        search_menu = self.page.locator("#_nkw")
        search_menu.click()
        search_menu.type(item)
        buttons = self.page.query_selector_all("button[class='btn btn--primary']")
        buttons[0].click()

        print("click on search button done successfully")