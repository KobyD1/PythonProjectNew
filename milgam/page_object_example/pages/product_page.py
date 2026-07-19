

class ProductPage:

    def __init__(self,page):
        print ("into product page")
        self.page = page

    def get_title(self):
        title = self.page.locator("div[class='app_logo']")
        return title.inner_text()

