import math
a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
print(d)
if d > 0:
    x1=(-b + math.sqrt(d)/(2*a))
    x2=(-b + math.sqrt(d)/(2*a))
    print(x1,x2)
elif d == 0:
    x=-b/(2*a)
    print(x)
else:
    print("Нет корней")

