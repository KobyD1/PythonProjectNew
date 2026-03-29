import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")

    shopping_button = page.locator("[class='layout-actionable link']").all()[0]
    shopping_button = page.locator("[class*='layout-actionabl']").all()[0]


    shopping_button_text =shopping_button.inner_text()
    index=shopping_button_text.index("bag")
    count = shopping_button_text[index+3:]
    count_1= shopping_button_text[-1:]







    print ("test end")

    browser.close()