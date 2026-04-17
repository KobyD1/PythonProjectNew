




def test_login_by_css(setup_playwright):
    print ("into swag labs")
    page =setup_playwright
    page.goto("https://www.saucedemo.com/")
    user = page.locator("input[class*='input_error']").first
    passowrd = page.locator("input[class*='input_error']").last

    user.click()
    user.fill("standard_user")

    passowrd.click()
    passowrd.fill("secret_sauce")

    login = page.locator("input[class='submit-button btn_action']")
    login.click()


    print ("test point")




