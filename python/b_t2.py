def gt(n):
    giai_thua = 1 
    for i in range(1, n+1):
        giai_thua = giai_thua * i
    return giai_thua

n =  int(input("n = "))
print("giai thua cua ",n," la ", gt(n))