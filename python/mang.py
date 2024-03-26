def selection_sort(arr, start, end):
    for i in range(start, end - 1):
        min_index = i
        for j in range(i + 1, end):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = []
num = int(input("Nhập một số (nhập 0 để dừng): "))

while num != 0:
    numbers.append(num)
    num = int(input("Nhập một số (nhập 0 để dừng): "))

size = len(numbers)
half_size = size // 2

selection_sort(numbers, 0, half_size)


selection_sort(numbers, half_size, size)
numbers[half_size:size] = numbers[half_size:size][::-1]



for i in range(half_size):
    print(numbers[i], end=" ")


for i in range(half_size, size):
    print(numbers[i], end=" ")

print()
