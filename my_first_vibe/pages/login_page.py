from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"


class LoginPage:
    """Page object for the Saucedemo login page."""

    def __init__(self, page: Page):
        self.page = page
        self._username = page.locator("#user-name")
        self._password = page.locator("#password")
        self._login_button = page.locator("#login-button")
        self._error = page.locator(".error-message-container h3")

    def goto(self) -> None:
        """Navigate to the login page."""
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str) -> None:
        """Perform login using provided credentials."""
        expect(self._username).to_be_visible()
        expect(self._password).to_be_visible()
        expect(self._login_button).to_be_visible()

        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()

    def expect_error_visible(self, expected_text: str | None = None) -> None:
        """Assert that an error message is visible; optionally check text."""
        expect(self._error).to_be_visible()
        if expected_text:
            expect(self._error).to_have_text(expected_text)
