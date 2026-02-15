class productPage():

    def __init__(self,page):
        self.page = page

    def verify_and_get_product_prices(self):
        prices = self.page.query_selector_all("[class='inventory_item_price']")
        prices_as_text = []
        for price in prices:
            price_as_str = price.text_content()
            print(price_as_str)
            price_as_str = price_as_str.replace("$", "")
            price_as_float = float(price_as_str)
            is_pass = price_as_float < 100  # getting results as boolean
            assert is_pass, "the Price is more than 100$"
            prices_as_text.append(price_as_str)
        print("after quesry selector all")
        return prices_as_text
