import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")

    shopping_button = page.locator("[class='layout-actionable link']").all()[0]
    # shopping_button = page.locator("[class*='layout-actionabl']").all()[0]

    time.sleep(3)
    shopping_button_text =shopping_button.inner_text()
    count_1= shopping_button_text[-1:]
    print ("0 was found in shopping_button text")
    assert count_1 == "1","1 was not found in shopping_button text"







    print ("test end")

    browser.close()