# files is list of string
# write a function that compare between each string to each string by the following
#  string letters must be equals but not at the same order 
# the output should be as the files string but without the not equals words
# example 
# files=["pool","loop","abc","cba","bbc","abcd","cab","poolp"]
# files=["pool","loop","abc","cba","cab"]

def word_compare (base, referance):

        base_sort = ''.join(sorted(base))  
        referance_sort=''.join(sorted(referance))
        if (base_sort == referance_sort):
            return True 
        else:
            return False
        
        
input_for_test = ["abc","bca","loop","pool","abcd","abbc","poolc",'oolp',"def","fed","acb"]
resut=[]

input_length = len(input_for_test)-1
for index in range (input_length):
   word_base= input_for_test[index]
   input_for_test.remove(word_base)
   for word_referance in input_for_test :
       is_include = word_compare(word_base,word_referance)
       if  (is_include):
           print(word_base)
           resut.append(word_base)
           break

   input_for_test.insert(index,word_base)
print ("###  End Part 1###")

print ('How to split by syntax')
sentence = 'Hi my name is John'
result_split = sentence.split(" ")
result_split_partial = sentence.split(" ",2)

print ("###  End Part 2###")

   
    
    
    
