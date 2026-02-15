

class TestSwaglabs:

    def test_swaglabs_correct_login(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"

    def test_swaglabs_by_class(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        #only in calss in case of space - sometimes it can be replaced by "."
        # e,g input_error.form_input.error instead of input_error form_input error
        elements = page.query_selector_all("[class*='input_error']")
        user= elements[0]
        password = elements[1]
        user.fill("standard_user")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        assert page.url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"


    def test_swaglabs_incorrect_password_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_incorrect_user_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_get_all_prices(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        list_prices = page.query_selector_all("[class='inventory_item_price']")
        first_price = list_prices[0]
        # print (first_price.inner_text())
        for price in list_prices:
            price_text = price.inner_text()
            price_text=price_text.replace("$", "")
            assert float(price_text) < 100, "Price text is higher VS max. level"
            # if float(price_text)<40 :
            #     print ("price is lower than 100$")
            print (price_text)

        print ("test end")
