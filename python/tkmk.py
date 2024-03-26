
tk1 = input("Vui long nhap tai khoan: ")
mk2 = int(input("Vui long nhap mat khau: "))

tk = 'minh'
mk = "190503"
dem = 1;
if(tk1 == tk and mk2== mk):
    print("Dang nhap thanh cong!")
else:
    for i in range(1,5):
        print("tai khoan hoac mat khau chua dung. Vui long nhap lai!")
        tk1 = input("Vui long nhap tai khoan: ")
        tk2 = int(input("Vui long nhap mat khau: "))
        if(tk1 == mk and mk1 == mk):
            print("Dang nhap thanh cong!")
        dem = dem +1
if(dem == 5):
    print("co cai tk ma khong nho la sao. Vui long thu lại sau 30p")


