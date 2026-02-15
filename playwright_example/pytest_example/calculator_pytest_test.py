


class TestCalculator():

    def test_select_category(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net")
        # calc = page.locator('a',  has_text="Age")
        # calc.click()
        print ("Test end")

