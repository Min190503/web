
hoc_phan = ['CS1', 'CS2', 'CS3', 'CS4', 'CS5']

# Khởi tạo các danh sách thống kê
students_1_hoc_phan = []
students_3_hoc_phan = []
students_5_hoc_phan = []
students_duoi_3_hoc_phan = []

# Nhập danh sách sinh viên đăng ký
students = input("Nhập danh sách sinh viên đăng ký, cách nhau bởi dấu phẩy: ").split(',')

# Thực hiện thống kê
for student in students:
    # Chuyển đổi mã sinh viên sang kiểu số nguyên
    student_id = int(student)
    
    # Nhập danh sách các môn học được sinh viên đăng ký
    danhsach_hocphan = input(f"Nhập danh sách các môn học mà sinh viên {student_id} đăng ký, cách nhau bởi dấu phẩy: ").split(',')
    
    # Đếm số lượng môn học mà sinh viên đăng ký
    dem_hocphan = len(danhsach_hocphan)
    
    # Thống kê số lượng sinh viên đăng ký 1 môn
    if dem_hocphan == 1:
        students_1_hoc_phan.append(student_id)
    
    # Thống kê số lượng sinh viên đăng ký 3 môn
    elif dem_hocphan == 3:
        students_3_hoc_phan.append(student_id)
    
    # Thống kê số lượng sinh viên đăng ký 5 môn
    elif dem_hocphan == 5:
        students_5_hoc_phan.append(student_id)
    
    # Thống kê số lượng sinh viên đăng ký dưới 3 môn
    elif dem_hocphan < 3:
        students_duoi_3_hoc_phan.append(student_id)

# In kết quả thống kê
print(f"Số lượng sinh viên đăng ký 1 trong 5 môn: {len(students_1_hoc_phan)}.")
print(f"Số lượng sinh viên đăng ký 3 trong 5 môn: {len(students_3_hoc_phan)}. Danh sách sinh viên: {students_3_hoc_phan}.")
print(f"Số lượng sinh viên đăng ký cả 5 môn: {len(students_5_hoc_phan)}. Danh sách sinh viên: {students_5_hoc_phan}.")
print(f"Số lượng sinh viên đăng ký dưới 3 môn: {len(students_duoi_3_hoc_phan)}. Danh sách sinh viên: {students_duoi_3_hoc_phan}.")