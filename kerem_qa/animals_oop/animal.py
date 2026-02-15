class Animal():
    def __init__(self):
        pass
        # print ("Into enimal constructor")
    def make_sound(self,sound):
        print (F"the animal make sound {sound}")

    def get_legs_from_db_into_animal(self,legs_amount):
        if legs_amount ==4 :
            print("You have 4 legs")

        else:
            legs_amount = 4
            print("legs changed to  4 legs")
        return legs_amount


    def calc_age(self):
        print("into calc age from animal")