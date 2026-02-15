from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.ebay.com")

    adv_button = page.get_by_role("link",name= "Advanced")
    adv_button.click()
    assert page.url =="https://www.ebay.com/sch/ebayadvsearch" ,"page URL is not as expected after clik on Adv. button"


    browser.close()
    print ("Test End")