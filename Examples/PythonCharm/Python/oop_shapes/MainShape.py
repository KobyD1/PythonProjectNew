from Examples.PythonCharm.Python.oop_shapes.ShapeParent import ShapeParent
from Examples.PythonCharm.Python.oop_shapes.circleChild import circleChild
from Examples.PythonCharm.Python.oop_shapes.squareChild import squareChild


class MainShape () :

    shape1 = ShapeParent("Shape White")
    shape2 = ShapeParent("Shape Blue")
    shape3 = circleChild("red")

    square = squareChild()
    shape1.perimeter(2,3)
    shape2.perimeter(4,5)
    square.area(3,4)




