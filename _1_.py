def myreplace(old_str, *args):
    for delimiter in args:
        old_str = old_str.replace(delimiter, '', 1)
    return old_str

n = input("n = ")
if myreplace(n, '-', '.').isdigit() == True:
    print(f"Result = {float(n)*3 + 1}")
else:
    print("Type again.")