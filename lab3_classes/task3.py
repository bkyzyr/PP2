class Shape:
    def area(self):
        return 0 

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape = Shape()
length = float(input("length of rectangle: "))
width = float(input("width of  rectangle: "))
rectangle = Rectangle(length, width)
print("Area is:", rectangle.area())
