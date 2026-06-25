import time
from playwright.sync_api import sync_playwright, expect

from winner_final.globals import FILTER
from winner_final.pages.playwright_main_ui import telesport_main_page

class PlaywrightMainUI():
    def __init__(self):
        pass


    def set_telesport_page(self, title_index, days_count,league="nba"):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.telesport.co.il/%D7%90%D7%96%D7%95%D7%A8%20%D7%95%D7%95%D7%99%D7%A0%D7%A8")
            telesport_page = telesport_main_page(page)
            for i in range(days_count):
                telesport_page.set_date()
                time.sleep(2)


            match title_index:
                 case 0:
                    print (" Run without filters ")
                 case 1:
                    telesport_page.set_table_filters(title_index)
                    telesport_page.set_table_league(league)


            table_data = telesport_page.get_table_content()
            l= len(table_data)
            print (57 * "*")
            print (f"******* Winner Analyzer Completed - found {l} games *******")
            print (57 * "*")

            return table_data


