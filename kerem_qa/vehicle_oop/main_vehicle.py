from kerem_qa.vehicle_oop.car import Car
from kerem_qa.vehicle_oop.motorcycle import Motorcycle
from kerem_qa.vehicle_oop.train import Train
from kerem_qa.vehicle_oop.vehicle import Vehicle

car_1 = Car(2023,"Nissan")
car_2 = Car(2020,"Cherry")
motor_1 = Motorcycle()
train = Train(True)
vehicle  = Vehicle()
car_2.get_years(2034)
car_1.car_tax_calc(3,120000)
distance_1  = car_2.calc_distance(1,60)
distance_train = train.calc_distance(1,140)
motor_1.tax_calc(4,45,80000)
vehicle.ticket_price(distance_1)
vehicle.ticket_price(distance_train)

print ("****Test End****")