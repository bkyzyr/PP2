import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

point1 = Point(2, 3)
point1.show() 

point1.move(5, 7)
point1.show() 

point2 = Point(1, 1)
print("Distance between point1 and point2:", point1.dist(point2))
