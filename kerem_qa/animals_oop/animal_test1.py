from kerem_qa.animals_oop.cat import Cat
from kerem_qa.animals_oop.dog import Dog

cat_1 = Cat("Sushi","Gray")
cat_2 = Cat("Hunny","White")
dog_1 = Dog("Shoko",5)

dog_1.calc_age()
cat_1.make_noise_by_cat()
cat_2.make_noise_by_cat()
cat_legs = cat_1.get_legs_from_db_into_animal(3)
dog_legs = dog_1.get_legs_from_db(5)
cat_2.get_legs_from_db_into_animal(6)
dog_1.make_sound("Hao")
if cat_legs == dog_legs:
    print ("Legs amount is equals")


dog_1.get_eyes_color()