def return_nth_value(L, a):
    L.sort()
    return_value = L[a]
    cnt = L.count(return_value)
    return (return_value, cnt)

list_input = list(int(x) for x in input("Nhap list: ").split())
a = int(input("Nhap a: "))
output = return_nth_value(list_input, a)

print(f"Co {output[1]} gia tri lon thu {a} trong list: {output[0]}.")
