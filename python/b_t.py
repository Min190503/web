def tinh_diem(DQT, DT,KT1,KT2):
    DQT = (KT1 + KT2) / 2
    Diem = DQT * 0.4 + DT * 0.6
    return Diem

KT1 = float(input("Nhập điểm kiểm tra 1: "))
KT2 = float(input("Nhập điểm kiểm tra 2: "))
DQT = (KT1 + KT2) / 2
DT = float(input("Nhập điểm thi cuối kỳ: "))
Diem = tinh_diem(DQT, DT)
print("Điểm học phần của bạn là:", Diem)