from PythonCharm.Python.oopAnimals.animal import animal
from PythonCharm.Python.oopAnimals.cat_stand_alone import cat_stand_alone
from PythonCharm.Python.oopAnimals.mouse import mouse
from PythonCharm.Python.oopAnimals.cat import cat




class main():
    dog1 = animal("Miles", 4)
    cat1 = cat_stand_alone("Cat",3)
    mouseTest= mouse("mouse1",2)
    cat2=cat("x",23,4)

    dog1.speak("hao")
    cat1.speak("mio")
    mouseTest.speak()
    legs = cat1.get_legs()
    cat1.get_legs()
    cat2.print_name()
    print (legs)