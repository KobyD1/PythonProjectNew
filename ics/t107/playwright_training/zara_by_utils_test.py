from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()
utils.playwright_start("https://www.zara.com/il/en/")

utils.playwright_stop()