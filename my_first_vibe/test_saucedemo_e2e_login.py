"""
End-to-end Playwright test for saucedemo login flow.
Tests successful login with credentials and verifies inventory page.
"""

import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


class TestSaucedemoLoginFlow:
    """Test suite for saucedemo login functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to the login page before each test."""
        page.goto(BASE_URL)
        self.page = page

    def test_successful_login_and_inventory_navigation(self):
        """
        End-to-end test: Login with valid credentials and verify successful navigation.
        
        Steps:
        1. Locate login form elements
        2. Verify form elements are visible
        3. Fill in username and password
        4. Click login button
        5. Verify URL navigation to /inventory.html
        6. Verify "Products" title is displayed
        """
        # Step 1: Locate login form elements using resilient selectors
        username_input = self.page.locator("#user-name")
        password_input = self.page.locator("#password")
        login_button = self.page.locator("#login-button")

        # Step 2: Verify login form elements are visible
        expect(username_input).to_be_visible()
        expect(password_input).to_be_visible()
        expect(login_button).to_be_visible()

        # Step 3: Fill in login credentials
        username_input.fill(USERNAME)
        password_input.fill(PASSWORD)

        # Step 4: Click the Login button
        login_button.click()

        # Step 5: Verify successful login by checking URL navigation to inventory page
        expect(self.page).to_have_url(EXPECTED_INVENTORY_URL)

        # Step 6: Verify the page title element contains "Products"
        title_element = self.page.locator('[data-test="title"]')
        expect(title_element).to_be_visible()
        expect(title_element).to_contain_text("Products")
