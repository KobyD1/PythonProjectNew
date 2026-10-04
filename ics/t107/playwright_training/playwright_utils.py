class PlaywrightUtils:


    def playwright_start(self,url):
        print ("Playwright start")
        from playwright.sync_api import sync_playwright, expect

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                args=["--start-maximized"]
            )
            page = browser.new_page()
            page.goto(url)

        return page

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




    def playwright_stop(self):
        print ("Playwright stop")



