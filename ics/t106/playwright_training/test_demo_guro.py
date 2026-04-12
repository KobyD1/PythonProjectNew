



def test_search_adv(setup_playwright):
    print ("into search by ebay")
    page =setup_playwright
    page.goto("https://demo.guru99.com/test/newtours/index.php")
    page.fill("[name='userName']", "tutorial")
    page.fill("[name='password']", "tutorial")
    page.click("[name='submit']")
    flights = page.get_by_role("link", name = "Flights")
    flights.click()

    if (page.locator("[class='cb-close']").count()>0):
        page.locator("[class='cb-close']").click()


    print ("fgdd")