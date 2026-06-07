date = "D5M08Y22"

index_1 = date.index("M")
index_2 = date.index("Y")
day = date[0:index_1]
month = date[index_1:index_2]
temp  = date[2:5]
year = date[index_2:]
new_date= f"{month}{day}{year}"
new_date= new_date.replace("M", "")
new_date= new_date.replace("D", "")
new_date= new_date.replace("Y", "")


print ("test end")