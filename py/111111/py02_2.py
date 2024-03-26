import math

def area(a,b,c):
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("Dien tich tam giac: ",area(a, b, c))
