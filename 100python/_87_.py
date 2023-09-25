def check_return(L, k):
    s = set(L)
    d = {item:L.count(item) for item in s}
    d = sorted(d.items(), key = lambda x: x[1])
    while(d[0][1] <= k):
        d.pop(0)
        if len(d) == 0:
            return []
    return [x for x,y in d]

list_input = list(int(x) for x in input("Nhap list: ").split())
output = check_return(list_input, int(input("Nhap k: ")))
if len(output):
    print(output)
else:
    print("Khong co gia tri thoa man.")