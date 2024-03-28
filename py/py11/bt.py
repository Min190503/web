input_string = input("Nhập dãy số, cách nhau bởi dấu cách hoặc tab: ")
numbers = input_string.split()
print("Dãy số vừa nhập:")
for number in numbers:
    print(number)