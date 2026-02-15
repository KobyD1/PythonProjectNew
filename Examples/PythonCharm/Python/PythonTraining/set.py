set1={1,2,3,4,5,8}
set2={4,5,6,7,8,9}


A = {'a', 'b', 'c', 'd'}
B = {'a', 'b'}
A.issubset(B)
C= set(A)
D=list(B) # casting to list
# find a-b
print (A-B)
print(A.difference(B))

# find the common , and action

set5=set2&set1
print (set5)

# join /or between 2 sets
set4=set1.union(set2)        #join/or
print(set4)

set4=set1|set2        #join
print(set4)

# find what is not common at both of sets
set5=set1.symmetric_difference(set2)
print(set5)

set15=set1^set2
print('set15',set15)

set1.symmetric_difference_update(set2)
print (set1)

set6=set1.intersection(set2)
print(set6)

