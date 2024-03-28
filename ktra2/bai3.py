n = int(input("Nhập giá trị N: "))

fib_dict = {}
a, b = 0, 1

for i in range(1, n+1):
    fib_dict[i] = a
    a, b = b, a+b

print(fib_dict)