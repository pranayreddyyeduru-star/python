import math

def circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius of the circle: "))

c = circumference(r)
print("The circumference of the circle is:", c)
