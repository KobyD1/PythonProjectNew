from PythonCharm.Python.oopAnimals.animal import animal


class  cat_stand_alone(animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_legs(self):
        print ("into get legs")
        return 4