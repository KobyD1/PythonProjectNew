from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")

    adv_button = page.get_by_text("Advanced")
    adv_button.click()
    url_adv= page.url
    print (url_adv)




    print ("test end")

    browser.close()