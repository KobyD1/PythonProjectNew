
cities_list=['haifa','Tel-Aviv','Jaffa','Ashdod','Ramat-Gan']
cities_list1=['Tel-Aviv']
print (cities_list[1])   # get value from place 1 
print (cities_list[1:3]) # get value between 1 to 3 
print (cities_list[-2])  # get value from 2 places before the last place  
print (cities_list[2:])  # get value from place 2 to the end of the list 
cities_list[:2]          # get value from the beginning up to place 2 
cities_list.append('Holon') # add 
cities_list.remove('haifa')
cities_list.insert(3,'Afula')  # add at spesific place
cities_list.__getitem__(1)
print (cities_list)
cities_list.extend(["5","6","7"])    # extend ,add more than single parameter to list 

print ('after extend to list -',cities_list) 


# sets , allow add and remove and join ,did not allow update 
cities_set={'haifa','Rome','Madrid'}
cities_set.add('London')
cities_set.remove('Rome')
cities_set.discard('Madrid')    # discard is remove but without error 
cities_set_update = {'Milano','Holon'}
for city in cities_set:
    print ('city from set is ',city)
citeis_all = cities_set.union(cities_set_update)    # join between 2 sets

set1 = {1, 2, 4,}
set2 = {4, 5, 6}

set3 = set1.difference(set1,set2)
# set4=set1.difference(set1,set2)
# print (citeis_all)
    
    
# tupple , did not allow to update delete or add  , allow join    
fruits_tupple1 = ('banana','apple','lemon')   
for fruit in fruits_tupple1:
    print (fruit)  
print (fruits_tupple1[0])   

fruits_tupple2 = ('Melon','Orange','WaterMelon') 
fruits_all = fruits_tupple1+fruits_tupple2    # join 

for fruit in fruits_all:
    print (fruit) 
    
fruit_list=list(fruits_all)   # casting is allowed from any type to any type 
fruit_set=set(fruits_all)
    

 