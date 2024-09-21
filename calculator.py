import random
import equasionSlover

x = random.randrange(-100, 100)
y = random.randrange(-100, 100)
z = random.randrange(-100, 100)

f = equasionSlover.calculate1(x)
print("Значення першої функції при аргументі " 
      + str(x) 
      + " є: \n" 
      + str(f))

r = equasionSlover.calculate2(x, y, z)
print("Значення другого виразу при аргументах X:" + str(x) 
      + " Y:" + str(y)
      + " Z:" + str(z)
      + " є: \n" 
      + str(r))
