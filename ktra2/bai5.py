
with open("D:/abc.txt", "r") as file:
    data = file.read()


numbers = []
for word in data.split():
    if word.isdigit():
        numbers.append(int(word))


with open("D:/number.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")


total = 0
with open("D:/number.txt", "r") as file:
    for line in file:
        number = int(line)
        total += number
        print(number)

print("Tổng các số: ", total)
