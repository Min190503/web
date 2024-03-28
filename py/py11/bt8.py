def sort_numbers(sequence):
    numbers = [int(x) for x in sequence.split(",")]

    # Sắp xếp các số chẵn giảm dần
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            max_even = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] % 2 == 0 and numbers[j] > numbers[max_even]:
                    max_even = j
            numbers[i], numbers[max_even] = numbers[max_even], numbers[i]

    # Sắp xếp các số lẻ tăng dần
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            min_odd = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] % 2 != 0 and numbers[j] < numbers[min_odd]:
                    min_odd = j
            numbers[i], numbers[min_odd] = numbers[min_odd], numbers[i]

    return numbers

# Nhập dãy số từ người dùng
sequence = input("Nhập dãy số (cách nhau bằng dấu phẩy): ")

# Sắp xếp lại dãy số theo quy tắc
sorted_sequence = sort_numbers(sequence)

# In ra màn hình dãy số đã được sắp xếp
print("Dãy số đã được sắp xếp:", ", ".join(str(num) for num in sorted_sequence))
