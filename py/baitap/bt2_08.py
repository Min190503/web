import math
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

except ValueError:
    print("Lỗi: a,b,c phải là số nguyên")


if(a+b <c or a+c < b , b+c <a):
    print("a,b hoặc c khongo thể là 1 cạnh của tam giác")
if(a<=0 or b <=0, c<= 0):
    print("a,b,c không thể là giá trị âm hoặc bằng 0")

p = (a+b+c)/2
print("Dien tich tam giac")
print(math.sqrt(p*(p-a)*(p-b)*(p-c)))

