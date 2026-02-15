

class loginPage():
    def __init__(self,page):
        self.page = page


    def login(self,user_text, password_text):
        user = self.page.locator("[id='user-name']")
        password = self.page.locator("[id='password']")
        login_button = self.page.get_by_text("Login")
        user.fill(user_text)
        password.fill(password_text)
        login_button.click()

    def verify_login_success(self):
        url = self.page.url
        assert url =="https://www.saucedemo.com/inventory.html","URL is not as expected after login success"

    def verify_login_fail(self):
        url = self.page.url
        assert url =="https://www.saucedemo.com/","URL is not as expected after login failed"

