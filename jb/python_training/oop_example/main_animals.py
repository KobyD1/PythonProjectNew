from jb.python_training.oop_example.cat_object import CatObject
from jb.python_training.oop_example.dog_object import DogObject


class MainAnimals:
    dog_1 = DogObject("Rexy",4)
    dog_2 = DogObject("Lucky",6)
    cat_1 = CatObject(4,8)

    dog_1.make_noise()
    dog_2.make_noise()
    dog_1.calculate_distance_at_parent(4,2)
    cat_1.make_cat_noise()
    cat_1.calculate_distance_at_parent(3,2)
    dog_1.calculate_distance_at_parent(3,6)