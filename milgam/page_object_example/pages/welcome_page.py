


class WelcomePage:
    def __init__(self,page):
        print ("into Welcome Page")
        self.page = page
        self.user_text = "standard_user"


    def login_by_user_password(self,user_text,password_text):
        print ("into login_by_user_password")
        user_name = self.page.locator("[id='user-name']")
        user_name.click()
        user_name.clear()
        user_name.fill(user_text)
        password = self.page.locator("[id='password']")
        password.fill(password_text)
        login_button = self.page.locator("[name='login-button']")
        login_button.click()


    def get_error_message(self):
        pass