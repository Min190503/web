import math

def area(a,b,c):
    p = (a+b+c)/2
    S = math.sqrt(p*(p+a)*(p+b)*(p+c))
    return S

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Dien tich tam giac là:",int(area(a, b, c)))