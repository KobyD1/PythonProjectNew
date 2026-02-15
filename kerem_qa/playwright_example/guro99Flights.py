from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/index.php")
    user  = page.locator("[name='userName']")
    password = page.locator("[name='password']")

    user.fill("tutorial")
    password.fill("tutorial")
    submit = page.get_by_role("Button",name="Submit")
    submit.click()
    flights = page.get_by_role("Link",name="Flights")
    flights.click()

    from_dropdown = page.locator("[name='fromPort']")
    from_dropdown.select_option("Paris")
    from_dropdown.select_option(index=1)
    print ("test end")