from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    print ("Test Start")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    print (page.url)
    page.goto("http://www.ebay.com")

    adv_button = page.get_by_text("Advanced")
    adv_button.click()
    url_adv= page.url
    print (url_adv)
    search_from_adv=page.locator("[id='_nkw']")
    search_from_adv.click()
    search_from_adv.fill("Shirt")



    print ("test end")

    browser.close()