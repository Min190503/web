def unique_substrings(S):
    substrings = set()

    def backtrack(start, current):
        if current not in substrings:
            substrings.add(current)

        for i in range(start, len(S)):
            backtrack(i + 1, current + S[i])

    backtrack(0, '')

    return substrings

# Nhập chuỗi S từ người dùng
S = input("Nhập chuỗi S: ")

# In ra tất cả các chuỗi con khác nhau của S
substrings = unique_substrings(S)
for substring in substrings:
    print(substring)
