

class productPage():
    def __init__ (self,page):
        self.page=page


    def get_first_product_price(self):
        prices = self.page.query_selector_all(".inventory_item_price")
        price_text = prices[0].text_content()
        price_text = price_text.replace("$","")
        price_as_float = float(price_text)
        assert price_as_float < 30, 'First product price is higher than 30$'







