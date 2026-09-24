class PlaywrightUtils:


    def playwright_start(self):
        print ("Playwright start")
        from playwright.sync_api import sync_playwright, expect

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                args=["--start-maximized"]
            )
            page = browser.new_page()
            page.goto("https://www.starbucks.com/")


    def playwright_stop(self):
        print ("Playwright stop")



