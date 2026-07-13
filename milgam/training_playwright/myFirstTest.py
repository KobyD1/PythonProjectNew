import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("[id='user-name']")
    user_name.click()
    user_name.clear()
    user_name.fill("standard_user")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_button = page.locator("[name='login-button']")
    login_button.click()
    time.sleep(2)
    num1=2
    num2=3
    summery = num1+num2
    assert summery >0 ,f"the value of summery is less than 0  -the summey is {summery}"
    assert num1> 0,f"the value of num1 is less than 0  -the num1 is {num1}"
    assert summery ==5 ,f"the value of summery is not as expected -the summey is {summery}"

    url = page.url
    assert url == "https://www.saucedemo.com/inventory.html","Page URL is not as expected"
    print (f"the url is {url}")



    print ("Test Successful")

    browser.close()