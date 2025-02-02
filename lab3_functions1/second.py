def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)

print(fahrenheit, celsius)
