from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")
    help=page.get_by_role(role="link",name="HELP")
    help.click()
    help_url= page.url
    if help_url=="https://www.zara.com/il/en/help-center":
        print ("test success")

    else:
        print ("test fail")




    page.close()
    print ("Test End")