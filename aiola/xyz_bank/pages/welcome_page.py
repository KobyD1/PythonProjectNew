import time

from playwright.sync_api import expect
from retry import retry
import calendar
from datetime import datetime, timedelta

from aiola.xyz_bank.commons.welcome_buttons import welcomeButtons


class welcomePage():
    def __init__(self, page):
        self.__page = page
        self.__title_locator = "[class='ng-binding']"
        self.__button_locator = "button.btn.btn-lg.tab"
        self.__amount = self.__page.locator("input[class^='form-control']")

        self.__form = self.__page.get_by_role("form")
        self.deposit_approve = self.__form.get_by_role("button", name="Deposit")
        self.__withdraw_approve = self.__form.get_by_role("button", name="Withdraw")
        self.__action_success_locator = "span.error.ng-binding"

    @retry(exceptions=AssertionError, tries=5, delay=0.5)
    def click_on_welcome_button(self, button: welcomeButtons):
        time.sleep(3)  # added due some stability issues , smart wait did not success to resolved them
        buttons = self.__page.query_selector_all(self.__button_locator)
        assert len(buttons) == 3, "One or more buttons(Deposit/Deposit/Transactions) into welcome page are missing"
        button = buttons[button.value]
        button.click()

    def set_deposit(self, amount: int) -> dict:
        print(f"Try to deposit {amount}")
        deposit_data = {}
        self.click_on_welcome_button(welcomeButtons.DEPOSIT)
        expect(self.deposit_approve).to_be_visible()

        self.__amount.click()
        self.__amount.fill(str(amount))
        self.deposit_approve.click()
        self.__page.wait_for_selector(self.__action_success_locator)
        deposit_data["date"] = self.get_date_as_string()
        deposit_data["amount"] = str(amount)
        deposit_data["type"] = "Credit"
        self.is_success_appears()
        return deposit_data

    def set_withdrawel(self, amount: int) -> dict:
        print(f"Try to withdrawel {amount}")
        withdrawel_data = {}
        self.click_on_welcome_button(welcomeButtons.WITHDRAWEL)
        expect(self.__withdraw_approve).to_be_visible()
        self.__amount.click()
        self.__amount.fill(str(amount))
        self.__withdraw_approve.click()
        self.__page.wait_for_selector(self.__action_success_locator)
        withdrawel_data["date"] = self.get_date_as_string()
        withdrawel_data["amount"] = str(amount)
        withdrawel_data["type"] = "Debit"
        self.is_success_appears()
        return withdrawel_data

    def get_balance(self):
        title = self.__page.query_selector_all(self.__title_locator)
        balance = title[1].text_content()
        return int(balance)

    def get_date_as_string(self) -> dict:
        present_day = datetime.now()
        month = calendar.month_name[present_day.month]
        date = present_day.strftime("%d, %Y %#I:%#M:%#S %p")
        if (date[0] == "0"):
            date = date[1:]
            print(date)
        date = month[:3] + " " + date
        return date

    def is_success_appears(self):
        assert self.__page.locator(
            self.__action_success_locator).is_visible(), "Success message did not appears as expected"
