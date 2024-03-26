"""stack = [] #Danh sách lưu trữ ký tự
chars_deltete = 0 #Số ký tự đã xóa

S = input("Nhap chuoi so: ")
N = input("So luong ky tu can xoa: ")


for char in S:
    while stack and chars_deltete < N and char > stack[-1]:
        stack.pop()
        chars_deltete = chars_deltete + 1
    stack.append(char)

while chars_deltete < N:
    stack.pop()
    chars_deltete = chars_deltete + 1

print("".join(stack))
"""



"""def remove_digits(S, N):
    stack = []  # Danh sách lưu trữ các ký tự
    chars_deleted = 0  # Số ký tự đã xóa

    for char in S:
        while stack and chars_deleted < N and char > stack[-1]:
            stack.pop()
            chars_deleted += 1
        stack.append(char)

    while chars_deleted < N:
        stack.pop()
        chars_deleted += 1

    return ''.join(stack)

# Nhập chuỗi S và số nguyên N từ bàn phím
S = input("Nhập chuỗi S: ")
N = int(input("Nhập số nguyên N: "))

result = remove_digits(S, N)
print("Chuỗi sau khi xóa ký tự:", result)
"""
S = input("Nhap chuoi S: ")
N = int(input("Nhap so nguyen N: "))

def remove_digits(S,N):
    stack = []
    n=chars_deleted = 0

    for char in S:
        while stack and chars_deleted < N and char > stack[-1]:
            stack.pop()
            chars_deleted += 1
        stack.append(char)

    while chars_deleted < N:
        stack.pop()
        chars_deleted +=1

    return "".join(stack)

print("Chuoi so sau khi xoa",remove_digits(S, N))
