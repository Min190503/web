import re

def is_valid_email(email):

    user_name = r'^[]+@[\w\.-]+\.\w+$'
    
    
    if re.search(user_name, email or tlu.edu or hotmail):
        return True
    else:
        return False


email_input = input("Nhập địa chỉ email: ")


if is_valid_email(email_input):
    print("Email hợp lệ.")
else:
    print("Email không hợp lệ.")
