def uc_check(n):
    if not(n.isdigit()):
        return False
    n = int(n)
    result = []
    for num in range(1, n):
        if n%num == 0:
            result.append(num)
    return result

a = input("Nhap a: ")
b = input("Nhap b: ")
result_a = uc_check(a)
result_b = uc_check(b)

if not(result_a) or not(result_b):
    print("Type again.")
else:
    print(f"Uoc cua a: {result_a}.")
    print(f"Uoc cua b: {result_b}.")
    uc = set(result_a).intersection(set(result_b))
    print(f"Uoc chung lon nhat cua a va b: {max(uc)}")