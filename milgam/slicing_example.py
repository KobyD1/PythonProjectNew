


city = "Petach-Tikva"
index = city.index("-")
prefix= city[:index]  # 0 set as a default
suffix = city[index+1:] # the length of the city  as default
suffix_1 = suffix[-3:]   # example how to define referance to the end of the text
prefix_2 =city[:-5]
prefix_3 = city[-5:-10]  # case of not logical values - it did not crashed
prefix_4 = city[+3:]   # example how to define referance to the begin  of the text

print ("end")