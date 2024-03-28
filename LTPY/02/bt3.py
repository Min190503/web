import math

def area2(xA,xB,xC,yA,yB,yC):
    Sabc = 0.5*abs((xB-xA)*(yC-yA)*(xC-xA)*(yB-yA))
    return Sabc

xA, yA = map(int, input("Nhập tọa độ điểm A(x, y): ").split())
xB, yB = map(int, input("Nhập tọa độ điểm B(x, y): ").split())
xC, yC = map(int, input("Nhập tọa độ diểm C(x, y): ").split())

print("Diện tích của tam giác ABC:",area2(xA, xB, xC, yA, yB, yC))

