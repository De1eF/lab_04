import math as m

def calculate1(x):
   try:
      return ((x-4)**3 + m.log(x)) / m.fabs(x + 1 / m.tan(x)) + m.cos(x+2)**3
   except ValueError:
      print("Хибний аргумент")

def calculate2(x,y,z):
   try:
      return 12 * (x**2 + m.sin(y)) + m.sqrt(z**2 + 1) / m.log(3, m.fabs(m.fabs(z) + 0.07))
   except ValueError:
      print("Хибний аргумент")
