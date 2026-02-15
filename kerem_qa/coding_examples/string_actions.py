full_name = "Leo Messi"  # how to define vartiables

index_1 = full_name.index(" ")
full_name_length = len(full_name)
# index_2 = full_name.index(" ",index_1+1,full_name_length-1) # example with start ,end

first_name = full_name[0:index_1]
first_name_by_slicing = full_name[:full_name_length]

last_name=full_name[index_1+1:full_name_length]   # adding 1 in ordr to remove the space in the beggining
last_name_by_slicing = full_name[index_1:]
print (F"last name is #{last_name}#")
print (first_name)
index_2 = full_name.index(" ")
sentence = ", Hi My name is Koby,I leave in Beer-Yaacov,the place Dalya best"
full_name = full_name.replace("Leo","Leonid")
words = sentence.split(" ")
index_3 = sentence.index("place")+6
place = sentence[index_3:-5]

print ("Test End")