
# list of alphabets
chars = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

for char  in chars :
    print (char)
# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, chars)
for char   in chars :
    print (char)
    
print ('XXXXXXXX')     
    
for x1 in filteredVowels :
    print(x1)
         
         
print (filteredVowels)         