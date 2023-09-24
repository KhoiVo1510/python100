def check_valid(*args):
    for num in args:
        if not(num.replace('.','', 1).replace('-','',1).isdigit()):
            return False
    return True
a = input("Nhap a = ")
b = input("Nhap b = ")
c = input("Nhap c = ")

if check_valid(a, b, c):
    lst = [float(a), float(b), float(c)]

    lst.sort()
    print(f"Sorted list: {lst}")

else: print("Type again.")

