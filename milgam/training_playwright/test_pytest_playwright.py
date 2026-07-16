

class TestPytestPlaywright():

    def test_swaglabs_login(self,setup_playwright):
        page =setup_playwright
        page.goto("https://www.saucedemo.com/")
        print ("test end")


