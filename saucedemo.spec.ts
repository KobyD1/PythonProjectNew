import { test, expect } from '@playwright/test';

test.describe('Saucedemo Login Flow', () => {
  const BASE_URL = 'https://www.saucedemo.com/';
  const USERNAME = 'standard_user';
  const PASSWORD = 'secret_sauce';

  test.beforeEach(async ({ page }) => {
    // Navigate to the login page before each test
    await page.goto(BASE_URL);
  });

  test('should successfully log in and navigate to inventory page', async ({ page }) => {
    // Step 1: Locate login form elements
    const usernameInput = page.locator('#user-name');
    const passwordInput = page.locator('#password');
    const loginButton = page.locator('#login-button');

    // Step 2: Verify login form elements are visible
    await expect(usernameInput).toBeVisible();
    await expect(passwordInput).toBeVisible();
    await expect(loginButton).toBeVisible();

    // Step 3: Fill in login credentials
    await usernameInput.fill(USERNAME);
    await passwordInput.fill(PASSWORD);

    // Step 4: Click the Login button
    await loginButton.click();

    // Step 5: Verify successful login by checking URL navigation to /inventory.html
    await expect(page).toHaveURL(/.*inventory\.html/);

    // Step 6: Verify the page title element contains "Products"
    const titleElement = page.locator('[data-test="title"]');
    await expect(titleElement).toBeVisible();
    await expect(titleElement).toContainText('Products');
  });
});
