A = input("Nhập dãy số A: ").split()
B = input("Nhập dãy số B: ").split()

A = list(map(int, A))
B = list(map(int, B))

min_number = float('inf')
found = False

for num in A:
    if num not in B and num < min_number:
        min_number = num
        found = True

if not found:
    print("không có")
else:
    vi_tri_cuoi = None
    for i in range(len(A)-1, -1, -1):
        if A[i] == min_number:
            vi_tri_cuoi = i
            break
    print("Số nhỏ nhất trong A nhưng không có trong B: ", min_number)
    print("Vị trí xuất hiện cuối cùng của số nhỏ nhất trong A: ", vi_tri_cuoi)
