import time

from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()
page = utils.playwright_start("https://www.zara.com/il/en/")
time.sleep(5)
page.url
print (page.url)

utils.playwright_stop()