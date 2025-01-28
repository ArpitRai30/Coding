import math
a = float(input("1st side of triangle: "))
b = float(input("2nd side of triangle: "))
c = float(input("3rd side of triangle: "))
s = (a + b + c) / 2
ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of triangle is: {ar:.4f}")