import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.metric-conversions.org/")

    drop_down = page.locator("[id='unitType']")

    drop_down.select_option("Speed conversion")
    time.sleep(3)

    act_url = page.url

    if act_url=="https://www.metric-conversions.org/speed-conversion.htm":
        print ("test success")

    else:
        print ("test failed")
        print ("act_url=",act_url)








    page.close()