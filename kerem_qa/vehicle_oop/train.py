from kerem_qa.vehicle_oop.vehicle import Vehicle


class Train(Vehicle):

    def __init__(self,is_light):
        self.is_light = is_light

    def get_pasengers(self,train_cars):
        pasengers = train_cars*50
        print (F"Max amount of pasengers: {pasengers}")