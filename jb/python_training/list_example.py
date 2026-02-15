names = ["Efratt", "Vered", "Moka","Max"]
grades = [78,79,56,89]
cities = ["Lod", "London","Paris","Lod", "Rome","Holon"]
cities.append("Milano")  # add milano to cities
cities.insert(3,"haifa")
cities.remove("haifa")
cities[2:4]
name = "Efrst"
short_name= name[1:3]

for name in names:
    print (name)
    l =len(name)
    print (f"the len of {name} is {l}")

city_index_1 = cities[1]
length_of_list = len(cities)
lod_counter = cities.count("Lod")
is_rome= "Rome" in cities
is_madrid = "Madrid" in cities

print (f"is_madrid is {is_madrid}")
print (f"is_rome is {is_rome}")

