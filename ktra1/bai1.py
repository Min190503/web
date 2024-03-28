
nhap_day_so = input("Nhập dãy số: ").split()

print("Dãy số vừa nhập:", ' '.join(nhap_day_so))

nhap_day_so = [float(num) for num in nhap_day_so]



max_number = max(nhap_day_so)
min_number = min(nhap_day_so)
print("Số lớn nhất trong dãy: ", max_number)
print("Số nhỏ nhất trong dãy: ", min_number)


sum_numbers = sum(nhap_day_so)
average = sum_numbers / len(nhap_day_so)
print("Tổng của dãy số: ", sum_numbers)
print("Trung bình cộng của dãy số: ", average)



count_0_3_9 = 0
count_4_5_4 = 0
count_5_5_6_9 = 0
count_7_8_4 = 0
count_8_5_10 = 0

for num in nhap_day_so:
    if num >= 0 and num <= 3.9:
        count_0_3_9 += 1
    elif num >= 4 and num <= 5.4:
        count_4_5_4 += 1
    elif num >= 5.5 and num <= 6.9:
        count_5_5_6_9 += 1
    elif num >= 7 and num <= 8.4:
        count_7_8_4 += 1
    elif num >= 8.5 and num <= 10:
        count_8_5_10 += 1

total_count = len(nhap_day_so)
day_so_0_3_9 = (count_0_3_9 / total_count) * 100
day_so_4_5_4 = (count_4_5_4 / total_count) * 100
day_so_5_5_6_9 = (count_5_5_6_9 / total_count) * 100
day_so_7_8_4 = (count_7_8_4 / total_count) * 100
day_so_8_5_10 = (count_8_5_10 / total_count) * 100

print("Tỉ lệ phần trăm các số trong khoảng 0-3.9: ", day_so_0_3_9, "%")
print("Tỉ lệ phần trăm các số trong khoảng 4-5.4: ", day_so_4_5_4, "%")
print("Tỉ lệ phần trăm các số trong khoảng 5.5-6.9: ",day_so_5_5_6_9, "%")
print("Tỉ lệ phần trăm các số trong khoảng 7-8.4: ", day_so_7_8_4, "%")
print("Tỉ lệ phần trăm các số trong khoảng 8.5-10: ", day_so_8_5_10, "%")
