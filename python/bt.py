a  = int(input('so tien gui = '))
s = 0
for i in range(10):
    a = a+a*0.051
print('So tien ban co sau 10 nam:',int(a))

for j in range(1000):
    a = a + a*0.051
    s = s +1
    if a == 50000000:
        print(s)