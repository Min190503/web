string = input("Nhập chuỗi: ")
n = string.split()
n.sort(key=str.lower,reverse=True)
print(n)