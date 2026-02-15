from PythonCharm.Python.oop_shapes.ShapeParent import ShapeParent

class squareChild(ShapeParent):

    def __init__(self):
        print ('into square')

    def get_area_from_db(self,color):
        print ('getting color from DB , color = '+color)