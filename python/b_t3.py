age = int(input("Nhap tuoi cua ban: "))
if(age<= 0 and age >120):
        print("Du lieu nhap vao khong hop le")
if(age > 0 and age < 13):
        print("Tre nho")
if(age >=13 and age < 18):
        print("Vi thanh nien")
if(age >= 18 and age < 25):
        print("Thanh nien")
if(age >= 25 and age <60):
        print("Nguoi truong thanh")
if(age >=60):
        print("Nguoi lon tuoi")
