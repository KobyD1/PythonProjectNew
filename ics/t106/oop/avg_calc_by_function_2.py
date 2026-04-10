from ics.t106.oop.utils106 import utils106

grades_1 = [60,45,36,89,78,90]

grades_2 = [607,435,356,879,778,90]

utils_106 = utils106()
utils_106.print_text("Test Start")
avg_1= utils_106.avg_calc(grades_1)
avg_2 = utils_106.avg_calc(grades_2)
if avg_1<avg_2:
    print ("avg_1 is bigger VS avg_2")

utils_106.print_text("Test End")