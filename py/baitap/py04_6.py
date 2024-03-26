a = input("str: ")
str = a.split(" ")
count = {}
for i in str:
    if i in count:
            count[i] += 1
    else:
        count[i] = 1
for i in count:
    print(i, count[i])

        