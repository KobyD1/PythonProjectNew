from playwright.sync_api import sync_playwright, expect


class PlaywrightUtils:

    def __init__(self):
        self.page = None
        self.browser = None
        self.p = None

    def playwright_start(self, url):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(url)
        return self.page

    def multiple_numbers(self, num1, num2):
        sum  = 0
        sum = num1 * num2
        print (f"sum = {sum}")

    def diff_numbers(self, num1, num2):
        if num1 > num2:
            res = num1 - num2
            print (f"result  = {res}")

        if num2>num1:
            res = num2 - num1
            print(f"result  = {res}")

        return res

    def add_numbers (self ,num_1,num2):
        sum = num_1 + num2
        if sum>10:
            print(f"sum = {sum} is greater than 10")
        else:
            print(f"sum = {sum} is less than 10")
        return sum




    def playwright_stop(self):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()
        if self.p:
            self.p.stop()
        print("Playwright stopped")



