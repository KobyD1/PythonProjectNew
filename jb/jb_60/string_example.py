
full_name = "Leo Messi"
index_1 = full_name.index(" ")
length= len(full_name)
first_name = full_name[:index_1]  # example for slicing from begining to index
last_name = full_name[index_1+1:length] # example of slicing from index to te end
last_name_1 =  full_name[index_1:]
full_name = full_name.replace("Leo", "Leonid")



full_name_updated = full_name.replace("ss","cc")
celeb= "Peer Tasi"
counter = celeb.count("e")
counter_T = celeb.count("T")

print (first_name)
print(last_name)
price = "25"
price_update = "25.7"
price_as_float = float(price_update)
price_as_int = int(price)   # casting - converting from string to int
final_price = price_as_int+4

shirt_price = 34
shirt_price_after_tax= 34+7
shirt_price_as_str = str(shirt_price)
length_shirt= len(shirt_price_as_str)

print ("test end")


