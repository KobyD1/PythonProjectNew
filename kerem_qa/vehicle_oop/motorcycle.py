from kerem_qa.vehicle_oop.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self):
        pass

    def tax_calc(self,years,tax_value,price):
       if years>5:
           price = price + tax_value

       print(F"Motorcycle price is {price}")
       return price


