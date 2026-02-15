from Examples.PythonCharm.Python.oop_shapes.ShapeParent import ShapeParent


class circleChild(ShapeParent):

    def __init__(self,color):
        self.color = color

    def print_color(self):
        print ('getting color from DB , color = '+self.color)

    def print_circle(self):
        print (f'this is a circle')
        self.print_color