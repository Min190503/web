try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    if b == 0:
        print("Lỗi: b phải khác 0")
    else:
        print("Giá trị phân số a/b là:", a/b)
except ValueError:
    print("Lỗi: a và b phải là số nguyên")