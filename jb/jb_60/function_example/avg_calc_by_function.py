from jb.jb_60.function_example.utils import utils

utils_instance=utils()

nums =[4,12,21,44,33,32,43]
utils_instance.avg_calc(nums)
num1= [34,66,55,3434]
avg1, size1= utils_instance.avg_calc(num1)
nums2 = [454,45,33,56]
avg2,size2 = utils_instance.avg_calc(nums2)
utils_instance.avg_calc([33,33,22,11])
if (avg2>avg1):
    print ("avg 1 was bigger")