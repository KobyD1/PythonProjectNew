


def test_search_product(setup_playwright):
    page  = setup_playwright
    page.goto("https://www.sephora.com/")
    counter = page.locator("svg[class='css-191rupl e15t7owz0']").count()
    if counter >0 :
        page.locator("svg[class='css-191rupl e15t7owz0']").click()



    print ("test end")

