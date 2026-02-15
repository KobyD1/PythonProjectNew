from kerem_qa.vehicle_oop.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,year,brand):
        self.year = year
        self.brand = brand


    def car_tax_calc(self,year,price):
        if year <2 :
            price = price +50

        else :
            price = price +150

        return price

    def get_years(self,current_year:str):
        years = current_year - self.year
        print(F"Years: {years}")
        return years

    def __private_example(self):
        print ("private example")