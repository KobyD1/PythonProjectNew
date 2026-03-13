from http.cookiejar import join_header_words
from json import JSONDecoder
from multiprocessing.queues import JoinableQueue

for i in range(0,20):
    print(i)
    i_new = i **2
    print(i_new)

    if (i == 6):
        continue  # jump to the begging of the loop
    if i_new > 25:
        print("the first number bigger than 25 is:" , i_new)
        break  # exit from loop

print("test end")




# John Due
#
# J
# Jo
# joh
# ...
