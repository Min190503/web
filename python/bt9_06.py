NS = input("Mã nhân viên phòng nhân sự: ").split()

HC = input("Mã nhân viên phòng hành chính: ").split()

TT = input("Mã nhân viên phòng truyền thông: ").split()

NV = set(map(int, NS + HC +TT))

print("Số nhân viên 3 phòng ban:",len(NV))
print("Nhân viên thuộc cả 3 phòng ban:",end = " ")
print( NS | HC | TT)