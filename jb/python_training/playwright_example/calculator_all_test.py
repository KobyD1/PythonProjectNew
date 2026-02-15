class TestCalculator():


    def test_calculator_bmi_button(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        bmi= page.get_by_text("BMI")
        bmi.click()
        assert page.url == "https://www.calculator.net/bmi-calculator.html", "BMI Page did not loaded after click on BMI button"
        print ("Test end")

    def test_calculator_get_by_role(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        payment_button  = page.get_by_role("link", name = "Payment Calculator" )
        payment_button.click()
        assert page.url == 'https://www.calculator.net/payment-calculator.html', "Payment Page did not loaded after click on Payment button"





