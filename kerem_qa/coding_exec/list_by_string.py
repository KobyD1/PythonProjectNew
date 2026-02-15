cites = ["TelAviv","Haifa","Barcelona","Rome","London"]
temp_city= ""
temp = 0
for city in cites:
    l = len(city)
    print (l)
    if l > temp :
     temp = l
     temp_city= city

print (temp_city)