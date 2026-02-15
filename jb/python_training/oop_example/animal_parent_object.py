

class AnimalParentObject():

    def calculate_distance_at_parent(self, time, speed):
        distance = time * speed
        if distance < 10:
            print("The animal is lazzy")

        else:
            print("the animal is ok")

        return distance