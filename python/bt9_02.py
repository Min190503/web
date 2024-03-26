
d = int(input("Ngay: "))
m = int(input("Thang: "))
y = int(input("Nam: "))

if(y %4 != 0 and y %100 == 0):
    if(m == 1 or m ==3 or m==5 or m==7 or m == 8 or m ==10 or m == 12):
        if (d > 31 or d < 0):
            print("Eror")
        if(d == 31):
            print("1","/",m+1,"/",y)
        else:
            print(d +1 ,"/",m,"/",y)
    if(m ==4 or m ==6 or m ==9 or m ==11):
        if (d> 30 or d < 0):
            print("Error")
        if(d == 30):
            print("1","/",m+1,"/",y)
        else:
            print(d+1,"/",m,"/",y)
    if(m == 2):
        if (d>29 and d <0):
            print("Eror")
        if(d == 28):
            print("1","/",m+1,"/",y)
if(y%4 == 0 and y%100 !=0):
    if(m == 1 or m ==3 or m==5 or m==7 or m == 8 or m ==10 or m == 12):
        if (d > 31 or d < 0):
            print("Eror")
        if(d == 31):
            print("1","/",m+1,"/",y)
        else:
            print(d +1 ,"/",m,"/",y)
    if(m ==4 or m ==6 or m ==9 or m ==11):
        if (d> 30 or d < 0):
            print("Error")
        if(d == 30):
            print("1","/",m+1,"/",y)
        else:
            print(d+1,"/",m,"/",y)
    if(m == 2):
        if (d>29 and d <0):
            print("Eror")
        if(d == 29):
            print("1","/",m+1,"/",y)
        

                    

            

        
        
        

    