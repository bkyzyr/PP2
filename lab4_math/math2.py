import math

h = float(input("height: "))
a = float(input("Base, first value"))
b = float(input("Base, second value"))

area = math.fsum([a, b]) * h / 2

print(f"Expected output: {area}")
