

class Vehicle:
    def __init__(self):
        print ("into Vehicle Class")

    def ticket_price(self,distance):
        if distance > 100:
            print ("You should pay the ticket")


    def calc_distance(self,time, speed):
        print (F"in calc distance with {time},{speed}")
        distance = time * speed

        return distance


