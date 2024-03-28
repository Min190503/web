def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] % 2 == 0 and numbers[j + 1] % 2 == 0 and numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            elif numbers[j] % 2 != 0 and numbers[j + 1] % 2 != 0 and numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

# Nhập dãy số từ người dùng
sequence = input("Nhập dãy số (cách nhau bằng dấu phẩy): ")
numbers = [int(x) for x in sequence.split(",")]

# Sắp xếp dãy số theo quy tắc chẵn giảm dần và lẻ tăng dần bằng thuật toán Bubble Sort
sorted_numbers = bubble_sort(numbers)

# In ra màn hình dãy số đã được sắp xếp
print("Dãy số đã được sắp xếp:", ", ".join(str(num) for num in sorted_numbers))
