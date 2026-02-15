from PythonCharm.Python.PythonTraining.privateUssage import person

print ('test start')
p1 = person('john','smith',35)
p2 = person ('David','Max',25)

p1.f_name="Sara"
p1._age = 33
print(p1.f_name,p1._age)
p1.__l_name = 'eee'
print(p1.__l_name)

