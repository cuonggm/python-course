# Ctrl / -> Comment
# ax^2 + bx + c
# import math
# math.sqrt(4)

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c

if delta < 0:
  print("Phuong trinh vo nghiem")
elif delta == 0:
  print("Phuong trinh co nghiem kep la: ", -b/(2*a))
else:
  print("Phuong trinh co 2 nghiem:", (-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a))

  # (x-1)(x-1) = x^2 - 2x + 1
