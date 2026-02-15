class person():
    def __init__(self,first_name,last_name,age):
        self.f_name = first_name
        self.__l_name = last_name    #private
        self._age = age              #protected



p1 = person ('John','Smith',35)
p2 = person ('Hong','Chai',33)
print (p1.f_name,",",p1._age)
p1_f_name = 'Max'
p1_age = 22
p1.__last_name = 'xxxx'
print ('afer update',p1.f_name,",",p1._age)

print ('stpo here')