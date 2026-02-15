class ProductPage:
    def __init__(self,page):
        self.page = page
        self.prices_text="abc"



    def get_first_price(self):

        list_prices = self.page.query_selector_all("[class='inventory_item_price']")
        prices = self.page.query_selector_all("[class='inventory_item_price']")
        self.prices_text

        first_price = list_prices[0].text
        print (f"first price found {first_price}")
        return first_price

    def get_all_prices(self):
        pass