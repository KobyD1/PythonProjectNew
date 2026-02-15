from jb.python_training.oop_vehicles.vehicle_parent import vehicleParent


class carObject(vehicleParent):


    def __init__(self,brand,is_electric):
        self.brand = brand
        self.is_electric = is_electric

    def battary_availble(self,capacity,ussage):
        if (self.is_electric==True):
            print ("trying to calculate the availble of battary")
            remaining_capacity = capacity - ussage
            return remaining_capacity

        else:
            return -1

