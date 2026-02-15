

class TestProduct():

    def test_verify_prices_less_than_100(self,setup_swaglabs):
        page,login_page,product_page = setup_swaglabs
        login_page.login("standard_user","secret_sauce")
        product_page.verify_product_prices()
