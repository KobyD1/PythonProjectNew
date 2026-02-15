print ('Please enter string to test')
string_to_test = input ()
temp = string_to_test

l = len(string_to_test)
for char in range(l):
    if (string_to_test[0] != string_to_test [l-1]):
        break
    else:
        string_to_test = string_to_test.replace(string_to_test[1],' ')
        string_to_test = string_to_test.replace(' ', '')
        print(string_to_test)