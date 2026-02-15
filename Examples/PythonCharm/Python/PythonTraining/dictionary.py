under_test={'FirstName':'John',
            'lastName':'Smith',
            'BornYear':1964,         
            'Gender':'Male'
            }
if 'o' in under_test['FirstName']:
    print ('first name include K')
if  ('aaa' == 'aaa') :
    print('equqls')
    
else :
    print ('K is not include in first name')    
    
if under_test['BornYear']<2000:
    print ('born year is before 2000')    
    
else :
    print('born year is after 2000')   
    
first_name = under_test.get('FirstName', 'aaaa') 
first_name1 = under_test.get('FirstName1','bbbbb')
print ('firstname=',first_name)
print ('firstname1=',first_name1)


    