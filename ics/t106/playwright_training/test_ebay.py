




def test_search_adv(setup_playwright):
    print ("into search by ebay")
    page =setup_playwright
    page.goto("https://www.ebay.com/")
    adv_button = page.get_by_text("Advanced")
    adv_button.click()
    url_adv = page.url
    print(url_adv)
    search_from_adv = page.locator("[id='_nkw']")
    search_from_adv.click()
    search_from_adv.fill("Shirt")

def test_search_main_menu(setup_playwright):
    print ("into search by ebay")
    page =setup_playwright
    page.goto("https://www.ebay.com/")
    search= page.locator("[id='gh-ac']")
    search.click()
    search.fill("Shirt")
