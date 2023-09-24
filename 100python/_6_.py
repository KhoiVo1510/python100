def myreplace(old_str, *args):
    for delimiter in args:
        old_str = old_str.replace(delimiter, '', 1)
    return old_str

def check(a):
    if a % 5 == 0:
        if (a < 20) or (a > 70):
            return True
    return False

a = input("a = ")
if myreplace(a).isdigit() == True:
    print(check(int(a)))
else:
    print("Type again.")