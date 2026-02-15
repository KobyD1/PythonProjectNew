from jb.python_training.oop_vehicles.car_object import carObject
from jb.python_training.oop_vehicles.truck_object import TruckObject

car_1 = carObject("Toyota", True)
car_2 = carObject("Mazda", False)
truck_1 = TruckObject("Volvo", 8)

car_2_price = car_2.price_calculator(340000,10,"UK")
car_price = car_1.price_calculator(470000, 18)
truck_price = truck_1.price_calculator_for_truck(300000)
prices = [120,230,123]
car_2.price_avg_calculator(prices)
# if car_price > truck_price:
#     print ("car price is higher than truck price")
assert car_price > truck_price, "car price is lower than truck price not as expected "

print("test end")
