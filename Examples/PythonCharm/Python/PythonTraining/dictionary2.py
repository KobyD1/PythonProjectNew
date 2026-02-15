key1='brand'
car= {
    key1:'Ford',
    'Model':'Focus',
    'Year':2012,         
                      }
brand_by_get= car.get('Brand')
brand = car.get('Brand', 'aaaa') 
brand_not_exist = car.get('BrandNotExist','Opel')
print('the value of key ',key1 ,'is ',car.get(key1))
print ('brand=',brand)
print ('brand_not_exist=',brand_not_exist)
print(car)
print ('get value without get command ',car['Brand']) 
del car['Year']
car ['newYear']=2014
print (car)
    