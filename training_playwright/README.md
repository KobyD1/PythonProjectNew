# Saucedemo Playwright Login Test

This directory contains an end-to-end test for https://www.saucedemo.com/ using Playwright and Pytest.

## Prerequisites

- Python 3.8+
- pip

## Installation

Install the required dependencies:

```bash
pip install playwright pytest pytest-playwright
playwright install
```

## Running the Tests

### Run all tests
```bash
pytest training_playwright/test_saucedemo_login.py -v
```

### Run with headed browser (see browser UI)
```bash
pytest training_playwright/test_saucedemo_login.py -v --headed
```

### Run with specific browser
```bash
pytest training_playwright/test_saucedemo_login.py -v --browser chromium
```

## Test Coverage

The test suite covers the login flow:

1. **Login**: Authenticates with `standard_user` / `secret_sauce`
2. **Verify Success**: Confirms login success by checking:
   - Inventory list is visible
   - 6 inventory items are displayed
   - Page title is "Swag Labs"
   - Logout link is visible (indicates logged-in state)

## Best Practices Applied

- **Web-First Assertions**: Uses `expect()` for assertions that wait intelligently
- **Resilient Locators**: Uses stable CSS selectors (IDs, semantic locators)
- **No Hardcoded Delays**: Uses Playwright's automatic waiting and visibility checks
- **Private Helper Methods**: Organized code for clarity
- **Fixture-Based Setup**: Uses pytest fixtures for browser management
- **Viewport Configuration**: Sets consistent viewport size for reproducibility
