import time

from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()

page = utils.playwright_start("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
time.sleep(3)
buttons  = page.query_selector_all('[class="btn btn-primary btn-lg"]')
button = buttons[1]
button.click()




utils.playwright_stop()