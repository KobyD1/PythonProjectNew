from PythonCharm.Python.oopAnimals.animal import animal


class cat(animal):
    def __init__(self,name,age,legs):
        self.name=name
        self.age=age
        self.legs=legs

    def print_name(self,pattern):
        name_internal = self.name
        owner='John'
        print ('i am ',pattern,' my owner is ',owner)