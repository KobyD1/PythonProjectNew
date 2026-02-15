import time


class TestCssExample():


    def test_wallmart_search(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/grade-calculator.html")
        grade_1 = page.locator("[name='s1']")
        grade_1.clear()
        grade_1.fill("77")
        calculate= page.query_selector_all("input[name='x'][type='submit']")
 # td:nth-child(1) > input[type=submit]
        calculate[0].click()
        results = page.locator("p[class='verybigtext']")
        results_text = results.inner_text()
        print ("Test end")





        print ("test end")