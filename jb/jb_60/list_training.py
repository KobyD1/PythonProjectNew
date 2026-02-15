# go over all cities in list
# find the length of each city
# find city that contains "-"
# when we got such city - stop the loop

cities = ["London", "Athen","New--York","Jerusalem","Lod" ]

for city in cities:
    print (city)
    print(f" the len found it {len(city)}")
    if (city.count("-")>0):
        print (f"- found at {city} ")
        break


prices = [12,45,67,32,34]