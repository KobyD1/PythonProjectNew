mylist = [1, 2, 3]
for i in mylist:
    print(i)
print ('Start print my list 1')
mylist1 = [x*x for x in range(5)]
for i in mylist1:
    print(i)

# generator - same as iterable, but can use only once , use (), did not store in memory
print ('Start print Generator')

mygenerator = (x * x for x in range(5))
for i in mygenerator:
    print (i)
print ('#### Start print Generator1 ###')
# generator - can use only once

for i1 in mygenerator:
    print (i1)
print ('#### end test ###')

