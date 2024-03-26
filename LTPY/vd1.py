import math
"""
#bạn có 10 triệu đồng trong tài khoản ngân hàng, với lãi xuất 5,1% hàng năm. Tính xem
#Sau 10 năm bạn có bao nhiêu 
#Sau bao nhiêu năm bạn sẽ có ít nhất 50tr

import math
tien = 10000000

for i in range(1,6):
    tien =tien +( tien * 0.051)
print("So tien cua ban sau 10 năm: ",int(tien))


dem =0
tien_gui = 10000000
while tien_gui <= 50000000:
    tien_gui = tien_gui +(tien_gui*0.051)
    dem = dem +1
print("So nam can: ",dem)
"""

#Nhập số nguyên X, hãy đếm xem X có bao nhiêu chữ số, in ra chữ số đầu tiên của X 

X = input("Nhập số nguyên X: ")
print("So luong phan tư cua X: ",len(X))

print("Phan tu dau tien cua X:",X[0:1])
