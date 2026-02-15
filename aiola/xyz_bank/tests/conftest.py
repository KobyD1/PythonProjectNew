import pytest

from aiola.xyz_bank.commons.globals import URL_BANK, BROWSER
from aiola.xyz_bank.pages.login_page import loginPage
from aiola.xyz_bank.pages.transactions_page import transactionsPage
from aiola.xyz_bank.pages.users_page import  usersPage
from aiola.xyz_bank.pages.welcome_page import welcomePage
from playwright.sync_api import sync_playwright, expect



@pytest.fixture()
def setup_browser():
    with sync_playwright() as playwright:
        if (BROWSER == 1):
            browser = playwright.chromium.launch(headless=False)
        else:
            browser = playwright.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(URL_BANK)
        login_page = loginPage(page)
        users_page = usersPage(page)
        welcome_page = welcomePage(page)
        transactions_page = transactionsPage(page)

        yield page , login_page, users_page ,welcome_page,transactions_page
        page.close()
        browser.close()
        print("Test end")

