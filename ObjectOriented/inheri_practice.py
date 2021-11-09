# common properties, Shape class k sobai use korba.
class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    def area(self):
        print("Area of method of shape class")

#Triangle class, Shape ar properties use korba. akana area method k override kora hoica.
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle: ",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ", area)

t1 = Triangle(20,30)
t1.area()

r2 = Rectangle(30,30)
r2.area()