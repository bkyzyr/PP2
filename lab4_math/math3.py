import math

sides = int(input("Input the number of sides: "))
lengthh = int(input("Input the length of a side: "))
area = int((sides * lengthh**2) / (4* math.tan(math.pi /sides)))
print("the area of the polygon is: ", area)