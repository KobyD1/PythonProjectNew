from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()

page = utils.playwright_start("https://www.starbucks.com/")

url = page.url

print (url)

utils.playwright_stop()