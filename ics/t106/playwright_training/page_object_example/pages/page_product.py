

class PageProduct():
    def __init__(self,page):
        print("### Page Product ###")
        self.page = page


    def get_prices(self):
        prices = self.page.query_selector_all('[class="inventory_item_price"]')
        first_price = prices[0]
        print(first_price.inner_text())

        for price in prices:
            text = price.inner_text()
            text = text.replace("$", "")
            print(f"price found the value is {text}")
            text_as_float = float(text)

    def set_drop_down(self):
        drop_down_sort = self.page.locator("[class='product_sort_container']")
        # drop_down_sort.select_option(index=2)
        drop_down_sort.select_option("Price (low to high)")

    def get_price_by_index(self):
        prices = self.page.query_selector_all('[class="inventory_item_price"]')
        price = prices[0].inner_text()
        print(f"found price the value is {price}")
        return price


