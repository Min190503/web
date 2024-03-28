kho_hang = {}
n = int(input("Nhập số lượng mặt hàng: "))
for i in range(n):
    item_name = input("Nhập tên mặt hàng: ")
    item_soluong = int(input("Nhập số lượng hàng tồn kho: "))
    kho_hang[item_name] = item_soluong

top_5_items = sorted(kho_hang, key=kho_hang.get, reverse=True)[:5]
print("Top 5 mặt hàng tồn kho nhiều nhất là:")
for item in top_5_items:
    print(item)

items_over_1000 = {item: soluong  for item, soluong  in kho_hang.items() if soluong  >= 1000}
print("\nCác mặt hàng có số lượng tồn kho lớn hơn hoặc bằng 1000 là:")
for item, soluong  in items_over_1000.items():
    print(item, soluong )

items_under_100 = {item: soluong  for item, soluong  in kho_hang.items() if soluong  < 100}
print("\nCác mặt hàng có số lượng tồn kho nhỏ hơn 100 là :")
for item, soluong  in items_under_100.items():
    print(item, soluong )