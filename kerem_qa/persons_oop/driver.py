from kerem_qa.persons_oop.person import Person


class Driver(Person):

    def __init__(self,license_level):
        self.license_level = license_level


    def get_license_level(self):
        print (F"license level found the value is {self.license_level}")
