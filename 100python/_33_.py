import math
def check_snt(n):
    if not(n.isdigit()):
        return False
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    for num in range(2, int(math.sqrt(n)) + 1):
        if n%num == 0:
            return False
    return True
a = input("Nhap so nguyen duong a: ")

if check_snt(a):
    print("a la so nguyen to")
else:
    print("a khong phai la so nguyen to")