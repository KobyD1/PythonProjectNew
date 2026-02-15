


class Test_calculator:


    def test_interset_drop_down(self, setup_playwright):



        page = setup_playwright
        page.goto("https://www.calculator.net")
        page.locator("[href='/interest-calculator.html']").click()
        dropdown=page.locator("[id='ccompound']")
        dropdown.select_option("weekly")
        dropdown.select_option(index=4)
        radio = page.locator("[id='cadditionat2']")
        radio.click()
        print ("test end")