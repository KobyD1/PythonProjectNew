import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_link=page.get_by_role(role="link",name="BMI Calculator")
    act_text =bmi_link.inner_text()
    bmi_link.click()
    act_url = page.url

    print (f"the URL is {act_url}")
    if act_url == "https://www.calculator.net/bmi-calculator.html":
        print ("test success")

    else:
        print ("test failed")
        print ("act_url=", act_url)



    time.sleep(2)











    print ("Test End")
    page.close()

