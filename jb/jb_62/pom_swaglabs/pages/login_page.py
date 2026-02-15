

class LoginPage():

    def __init__(self, page):
        self.page = page

    def set_user_and_password(self,user_text="standard_user" , password_text="secret_sauce"):
        user = self.page.locator("#user-name")
        password = self.page.locator("#password")
        user.fill(user_text)
        password.fill(password_text)


    def click_on_login(self):
        login = self.page.get_by_text("Login")
        login.click()
