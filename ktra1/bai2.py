
hoc_phan = ['CS1', 'CS2', 'CS3', 'CS4', 'CS5']


students_1_hoc_phan = []
students_3_hoc_phan = []
students_5_hoc_phan = []
students_duoi_3_hoc_phan = []


students = input("Nhập danh sách sinh viên đăng ký, cách nhau bởi dấu phẩy: ").split(',')


for student in students:
   
    student_id = int(student)
   
    danhsach_hocphan = input(f"Nhập danh sách các môn học mà sinh viên {student_id} đăng ký, cách nhau bởi dấu phẩy: ").split(',')
   
    dem_hocphan = len(danhsach_hocphan)
 
    if dem_hocphan == 1:
        students_1_hoc_phan.append(student_id)
    
    elif dem_hocphan == 3:
        students_3_hoc_phan.append(student_id)
    
   
    elif dem_hocphan == 5:
        students_5_hoc_phan.append(student_id)
    
    elif dem_hocphan < 3:
        students_duoi_3_hoc_phan.append(student_id)


print(f"Số lượng sinh viên đăng ký 1 trong 5 môn: {len(students_1_hoc_phan)}.")
print(f"Số lượng sinh viên đăng ký 3 trong 5 môn: {len(students_3_hoc_phan)}. Danh sách ma sinh viên: {students_3_hoc_phan}.")
print(f"Số lượng sinh viên đăng ký cả 5 môn: {len(students_5_hoc_phan)}. Danh sách ma sinh viên: {students_5_hoc_phan}.")
print(f"Số lượng sinh viên đăng ký dưới 3 môn: {len(students_duoi_3_hoc_phan)}. Danh sách ma sinh viên: {students_duoi_3_hoc_phan}.")