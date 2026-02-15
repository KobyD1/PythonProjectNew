class ShapeParent:

    def __init__(self,name):
        self.name = name

    def area(self,x,y):
        print('calculate area of shape')
        area = x * y
        return area

    def perimeter(self,x,y):
        print('calculate perimeter of shape')
        peri = 2*x + 2*y
        return peri
