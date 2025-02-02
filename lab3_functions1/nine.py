import math 
def func(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
radius = float(input())
print(func(radius))