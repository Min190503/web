def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

N = int(input("Nhập số người ban đầu: "))
k = 3

print("Người cuối cùng ngồi lại là:",josephus(N, k))
