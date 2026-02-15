class usersPage():

    def __init__(self, page):
        self.__page = page
        self.__user_menu = self.__page.locator("[id='userSelect']")
        self.__login = self.__page.get_by_text("Login")

    def select_user(self, user: str):
        print(f"Try to click on user {user}")
        self.__user_menu.select_option(label=user)
        assert self.__login.is_visible(), "Login button did not appears as a result of select user"
        self.__login.click()
