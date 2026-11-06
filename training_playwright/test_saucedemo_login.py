"""
End-to-end Playwright test for https://www.saucedemo.com/
Scenario: User login and verify success.
"""

import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


class TestSaucedemoLogin:
    """E2E tests for Saucedemo login flow."""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to the site before each test."""
        page.goto(BASE_URL)
        self.page = page

    def test_login_success(self):
        """
        Test successful login:
        gov_1. Log in with standard_user and secret_sauce
        2. Verify login success by checking inventory page is displayed
        """
        # Perform login
        self._login()

        # Verify login success
        self._verify_login_success()

    def _login(self):
        """Log in with standard_user credentials."""
        username_input = self.page.locator("#user-name")
        password_input = self.page.locator("#password")
        login_button = self.page.locator("#login-button")

        expect(username_input).to_be_visible()
        expect(password_input).to_be_visible()
        expect(login_button).to_be_visible()

        username_input.fill(USERNAME)
        password_input.fill(PASSWORD)
        login_button.click()

    def _verify_login_success(self):
        """Verify login was successful by checking for inventory page elements."""
        # Wait for inventory list to be visible
        inventory_list = self.page.locator(".inventory_list")
        expect(inventory_list).to_be_visible()

        # Verify inventory items are displayed
        inventory_items = self.page.locator(".inventory_item")
        expect(inventory_items).to_have_count(6)

        # Verify page title contains "Swag Labs"
        expect(self.page).to_have_title("Swag Labs")

        # Verify logout link is visible (indicates logged-in state)
        logout_link = self.page.locator("#logout_sidebar_link")
        expect(logout_link).to_be_visible()
