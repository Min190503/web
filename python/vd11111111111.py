x = input("Nhap số phần tử ").split()
a= set(map(int, x))
for i in a:
    print(i)
print("Số phần tử của tập hợp:",len(a))
print("Giá trị lớn nhất của tập hợp:",max(a))
print("Giá trị nhỏ nhất của tập hợp:",min(a))
