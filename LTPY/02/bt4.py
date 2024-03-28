

def total(N):
    s = 0
    while N > 0:
        a = int(N % 10)
        s = s + a
        N = N/10
    return s

N = int(input("N = "))
print("Tổng của số phần tử:",total(N))
