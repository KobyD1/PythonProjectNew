from jb.python_training.oop_vehicles.vehicle_parent import vehicleParent


class TruckObject(vehicleParent):

    def __init__(self,brand,weels_amnount):
        self.brand = brand
        self.wheels_amount = weels_amnount

    def calculate_distance(self,time , speed):
        distance  = time * speed
        return distance

    def price_calculator_for_truck(self,price):
        total_price = price * 1.18
        print (f"the total price is {total_price}")
        return total_price