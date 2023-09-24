def check_value(tri_val):
    for val in tri_val:
        if not(val.replace('.', '', 1).isdigit()):
            return False
    return True

def check_tri_type(tri_val):
    a = tri_val[0]
    b = tri_val[1]
    c = tri_val[2]
    if not((a > abs(b-c)) and (a < (b+c))\
    and (b > abs(a-c)) and (b < (a+c))\
    and (c > abs(a-b)) and (c < (a+b))):
        return "Day khong phai la tam giac"
    
    if len(set(tri_val)) == 1:
        return "Day la tam giac deu"
    elif len(set(tri_val)) == 2:
        if 2*(a**2) == c**2:
            return "Day la tam giac vuong can"
        else:
            return "Day la tam giac can"
    else:
        if a**2 + b**2 == c**2:
            return "Day la tam giac vuong "
        else:
            return "Day la tam giac thuong"
    
            
    
print("Nhap do dai 3 canh tam giac a, b, c:")
lst_check = [input("a = "), input("b = "), input("c = ")]

if check_value(lst_check):
    lst_check = list(map((lambda num: float(num)),lst_check))
    lst_check.sort()
    print(check_tri_type(lst_check))
else:
    print("Invalid type.")