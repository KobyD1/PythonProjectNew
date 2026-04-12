

def test_search_adv(setup_playwright):
    print ("into search by ebay")
    page =setup_playwright
    page.goto("https://www.calculator.net/interest-calculator.html")
    initial = page.locator("[id='cstartingprinciple']")
    initial.click()
    initial.clear()
    initial.fill("2323")
    print ("eeeer")
