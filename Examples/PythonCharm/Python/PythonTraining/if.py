from test.test_largefile import size

countries = ["Israel", "Usa", "France", "Italy"]
cities = ["London", 'Paris', 'Rome', 'Milano']
print(countries.count('Usa'))
print(' index found value =', countries.index('France'))
sizeBefore = len(cities)
cities.insert(2, 'Haifa')  # add to cities
cities.append('Holon')
cities[3]
sizeAfter = len(cities)

if cities[2] == 'Haifa':  # compare to string
    print('haifa found at place # 2 by compare to string ')

if sizeAfter > sizeBefore:
    print('size after equals to', sizeAfter)

count = 0
for city in cities:
    count += 2   # add 2 to count every interaction
    print(city, ' found at place#', count)

if count > 10:
    print('the value of count is', count)
else:

    print('else found ')

sum = 0
print('**** start last loop *****')
for x in range(2, 20, 2):  # loop in range with step
    sum = sum + x
    if sum > 50:
        print('The value of sum is >50 ,x=', x)

    else:
        print('sum is >50,x=', x)

print('the value of sum is', sum)

