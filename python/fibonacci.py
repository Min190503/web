import math
n = int (input ("Vui lòng nhập giá trị số nguyên để kiểm tra số Fibonacci:"))
def isFibo (m):
    n = int (math.sqrt (m))
    return n * n == m
def kt_fibo (m ):
    return isFibo (5 * m * m + 4) or isFibo (5 * m * m - 4)
if (kt_fibo (n) == True): print (n, "là số Fibonacci")
else: print (n, "không phải là số Fibnacci")