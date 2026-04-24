


class PageWelcome():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_user(self):
        print("### set  User ###")
        user = self.page.locator('[name="user-name"]')
        user.click()
        user.fill("standard_user")

    def set_password(self):
        print("### Set Password ###")
        password = self.page.locator('[name="password"]')
        password.click()
        password.fill("secret_sauce")

    def set_login(self):
        user = self.page.locator('[name="user-name"]')
        user.click()
        user.fill("standard_user")
        password = self.page.locator('[name="password"]')
        password.click()
        password.fill("secret_sauce")
        login_button = self.page.get_by_text("Login")
        login_button.click()




