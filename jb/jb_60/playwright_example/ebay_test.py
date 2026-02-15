from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")
    adv= page.get_by_role("link",name='Advanced')
    adv.click()




    browser.close()
    print ("Test End")