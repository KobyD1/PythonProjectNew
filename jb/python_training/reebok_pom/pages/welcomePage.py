class WelcomePage():

    def __init__(self,page):
        self.page = page

    def search_for_item(self):
        print ("trying to search fopr item")
        search_icon = self.page.locator("[id='header-search']")
        search_icon.click()
        locetors = self.page.query_selector_all("[name='q']")
        search_menu = locetors[1]
        search_menu.click()
        search_menu.fill("Shirt")


    def click_on_close_popup(self):\
            self.page.locator("[class='spicegems_cr_icon_close_Svg']").click()