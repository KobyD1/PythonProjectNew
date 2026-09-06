cities = ["Lod","Jerusalem","Rome","Madrid","London","Eilat"]
temp = 0

for city in cities:
    l = len(city)
    print (len(city),"is the length of ",city)
    if l > temp:
        temp = len(city)

print (temp,"#### is longest city length ",city)