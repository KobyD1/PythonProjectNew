

def test_login_correct_details(setup_playwright_swaglabs):
    page = setup_playwright_swaglabs
    page.goto("https://www.saucedemo.com/")
