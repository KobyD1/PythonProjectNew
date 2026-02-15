from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    password = page.locator("[name='password']")
    password_by_id = page.locator("[id='password']")
    login_button = page.locator("[id='login-button']")

    user.click()
    user.clear()
    # user.fill("standard_user")
    user.type("standard_user")



    password.click()
    password.clear()
    password.fill("secret_sauce")

    login_button.click()
    url=page.url
    print (f"page url is {url}")
    assert url =='https://www.saucedemo.com/inventory.html',"Page URL is not as expected after login "


    page.close()
    print ("Test End")