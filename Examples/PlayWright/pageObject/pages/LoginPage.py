from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("//input[@type='text']")
        self.password = page.locator("//input[@type='password']")
        self.login_button = page.locator("text=LOGIN")
        self.home_button = page.locator("button[id=react-burger-menu-btn]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.home_button).to_be_visible()