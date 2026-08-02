# Project Guidelines & Agent Skills
## Agent Execution Instructions

You are equipped with specialized project agents located in `agents.md`.

## Execution Rules:
1. When the user specifies an agent name (e.g., `PlaywrightAgent:`, `@PlaywrightAgent`, or `CodeReviewAgent:`), read and adopt the matching personality, constraints, and instructions defined in `agents.md`.
2. when the user does not specify an agent, default to `CodeReviewAgent` for UI test generation and automation tasks.
3. when the user does specify an not exist  agent,please respond with a clear error message indicating that the agent is not recognized and provide a list of available agents from `agents.md`.
2. Follow all locators, assertions, and execution rules specified under that agent section in `agents.md`.
## Core Frameworks & Stack
- **Language**: Python 3.12+
- **Testing Framework**: Pytest with `pytest-playwright`
- **Automation Focus**: Playwright for Web UI Testing

## Coding Standards & Best Practices
- Follow **PEP 8** naming conventions and standard Python formatting.
- Always use explicit element locators in Playwright (e.g., `page.get_by_role()`, `page.get_by_test_id()`) over rigid XPath or generic CSS selectors.
- Avoid hardcoded timeouts (like `time.sleep()`). Always use Playwright auto-waiting or explicit `expect()` assertions.
- Keep tests modular using the **Page Object Model (POM)** pattern where applicable.
- allways use `pytest` fixtures for setup and teardown of test environments.
- allays use assert to find the expected results in the tests.
- allways provide explanation to the error 

## Agent Behavior & Code Fixes
- When asked to fix code or errors, apply the solution directly to the file without conversational filler, lengthy explanations, or unnecessary summaries.
- Preserve existing logic and docstrings unless explicitly told to refactor them.
- Do not add debug `print()` statements in production or test files; use standard logging or Pytest assertions instead.

