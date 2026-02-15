def is_last_eq_to_start(pattern_to_test):
    cntr= int(len(pattern_to_test)/2)
    for letter in range (cntr):
        begin  = pattern_to_test[letter]
        end  = pattern_to_test[len(pattern_to_test)-letter]
        if (begin==end):
            print('match found')


first_test = "abbccbba"
print(first_test)
is_last_eq_to_start(first_test)
first_test.replace()
