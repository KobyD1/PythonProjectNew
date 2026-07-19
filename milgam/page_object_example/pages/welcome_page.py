


class WelcomePage:
    def __init__(self,page):
        print ("into Welcome Page")
        self.page = page
        self.user_text = "standard_user"


    def login_by_user_password(self):
        print ("into login_by_user_password")
        user_name = self.page.locator("[id='user-name']")
        user_name.click()
        user_name.clear()
        user_name.fill("standard_user")
        password = self.page.locator("[id='password']")
        password.fill("secret_sauce")
        login_button = self.page.locator("[name='login-button']")
        login_button.click()


    def get_error_message(self):
        pass