# GitHub Copilot Instructions - Playwright & Pytest Automation

## General Philosophy
- **Robustness Over Speed:** Prioritize test stability and resilience. Avoid flaky tests.
- **Python & Type Hints:** Write clean Python code following PEP 8 with explicit type hints for all function arguments, return types, and class attributes.
- **Prefix:** Only the first message at chat  message will start with "Hi Koby" 
- **Suffix:** every message will end with "Thanks!" and the name of the agent that is responding. For example, "Thanks! @playwright-agent" or "Thanks! @api-agent".
- **Agents:** in case of coding response Use the appropriate agent for the task. For example, use `@playwright-agent` for UI automation and `@api-agent` for API testing.
- **Explanations:** do not provide explanations or reasoning unless explicitly requested. Only provide code and instructions.



## Locator Strategy (Strictly NO XPATH)
- **Zero XPath Policy:** XPath locators are **strictly forbidden** under any circumstances. Never generate or suggest XPath expressions.
- **Preferred Locator Hierarchy:** Use the following locator types in order of preference:
  1. **Semantic Playwright Locators:** Use built-in user-facing methods when applicable (`page.get_by_role()`, `page.get_by_label()`, `page.get_by_placeholder()`).
  2. **ID:** Use element IDs when available (`page.locator("#element-id")` or `page.get_by_test_id(...)`).
  3. **Name:** Use name attributes (`page.locator("[name='username']")`).
  4. **Class :** Use class names for styling hooks (`page.locator(".btn-primary")`).
  5. **CSS Selectors:** Use clean, specific CSS selectors  (` page.locator("button[class='primary']")`).
  
- **Clean Selectors:** Keep CSS selectors maintainable and avoid overly long or brittle descendant chains.

## Playwright Best Practices
- **Auto-Waiting:** Rely on Playwright's built-in auto-waiting mechanism. **Never** use `time.sleep()` or hardcoded delays. Use proper assertions (`expect(locator).to_be_visible()`) instead.
- **Page Object Model (POM):** Structure test automation using the Page Object Model design pattern. Keep locators and actions inside Page classes, and assertions inside the test files.

## Pytest Standards & Structure
- **Naming Conventions:** Test files must start with `test_` (e.g., `test_login.py`), test functions must start with `test_`, and Page classes should be PascalCase (e.g., `LoginPage`).
- **Fixtures & Conftest:** Use `conftest.py` for setup/teardown logic, browser context management, and reusable fixtures.
- **Parametrization:** Use `@pytest.mark.parametrize` for data-driven testing where applicable.

## Error Handling & Reporting
- **Explicit Assertions:** Write clear failure messages in assertions (e.g., `assert element.is_visible(), "User dashboard failed to load after login"`).
- **Clean Code & Docstrings:** Add concise docstrings to test functions describing what scenario is being validated.