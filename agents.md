# Agent Directives & Operational Workflows
# Agents

## PlaywrightAgent
**Purpose:** Generate Playwright UI tests and browser automation scripts  
**Handles:** playwright, ui test, browser automation  
**Input:** Description of a UI flow or test scenario  
**Output:** Playwright test code (Python)
## Agent Capabilities & Execution Rules
- **Autonomous Fixes**: When asked to fix errors, modify code files directly using your file editing tools.
- **Concise Response Rule**: Do NOT provide conversational intros, summaries, or post-fix explanations unless explicitly requested. Apply the code fix cleanly.
- **Terminal Operations**: 
  - Execute test runs using `pytest` from the terminal when requested.


## Code & Test Quality Standards
- **Locators**: Prefer resilient Playwright locators:
  - `page.get_by_role()`
  - `page.get_by_test_id()`
  - `page.get_by_label()`
  - *Avoid rigid XPath or brittle relative CSS selectors.*
- **Assertions**: Always use Playwright web-first assertions (`expect(locator).to_be_visible()`) instead of raw Python `assert` statements for UI elements.
- **No Hardcoded Delays**: Never use `time.sleep()`. Rely strictly on Playwright's auto-waiting mechanisms and explicit `expect()` timeouts.
- **Code Cleanliness**: Remove unused imports, type hints where applicable, and avoid adding `print()` statements—use standard logging or assertions.





## CodeReviewAgent
**Purpose:** Analyze code, detect issues, suggest improvements  
**Handles:** review, refactor, analyze, clean code  
**Input:** Code snippet or file  
**Output:** List of issues + recommended fixes






