from jb.python_training.oop_university.person_parent import PersonParent


class Driver(PersonParent):
    def __init__(self,name:str,license:str):
        self.name=name
        self.license=license


    def get_vehicles_vs_license(self):
        if self.license=="a" :
            print ("you allowed to use motorcycle only")

        elif self.license=="b":
            print ("you allowed to use car and motorcycle")

        elif self.license=="c":
            print ("you allowed to use truck")

        else:
            print ("your license did not recorgnised")