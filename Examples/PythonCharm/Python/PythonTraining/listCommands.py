
def print_list (list_to_print):
    print(list_to_print)

# list of alphabets
alphabets = ['a', 'b', 'd', 'i', 'o', 'e', 'o']
print (len(alphabets))
alphabets.append('f')       # add at the last place
alphabets.insert(2,'c')     # add c at place 2 in addition to other, the length will increased
print (alphabets[2])
print (len(alphabets))
print_list(alphabets)
alphabets.remove('a')
print_list(alphabets)
alphabets.sort()
print_list(alphabets)
alphabets[0] = 'aa'        # replace at index 0
#scan list
for x in range (len(alphabets)):
    print('the value at place ',x,'is ',alphabets[x])
print ('brfore loop')
for alphabet in alphabets:
    print (alphabet)
