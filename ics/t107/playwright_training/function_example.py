from ics.t107.playwright_training.playwright_utils import PlaywrightUtils

utils = PlaywrightUtils()

utils.multiple_numbers(2,7)
res_1 = utils.diff_numbers(5, 90)
res_2 = utils.diff_numbers(15, 8)
res_3 =utils.add_numbers(5, 8)
res_4 = utils.add_numbers(15, 9)


if res_1  > res_2:
    print(res_1)
