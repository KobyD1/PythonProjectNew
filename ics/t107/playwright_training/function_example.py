from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()

utils.multiple_numbers(2,7)
res_1 = utils.diff_numbers(5, 90)
res_2 = utils.diff_numbers(15, 8)

if res_1  > res_2:
    print(res_1)
