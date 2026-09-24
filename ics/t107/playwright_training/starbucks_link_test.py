import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.starbucks.com/")
    gift_card = page.get_by_role(role = "link",name="GIFT CARDS")



    gift_card.click()
    url = page.url
    print (f"url is {url}")
    if "gift" in url:     # example how to find if gift is in url
        print ("URL found ")

    else:
        print ("URL not found ")


    page.close()