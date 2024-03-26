def ktr(S):
    a = ""
    for char in S:
        if char.isdigit():
            a += '?'
        else:
            a += char
    return a

S = input("str: ")
print(ktr(S))

        

