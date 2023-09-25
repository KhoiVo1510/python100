def ex88(lst, k):
    fullfilled_lst = []
    for i in range(len(lst)):
        t_lst = lst[i:len(lst)]
        while(len(t_lst) != 0):
            if sum(t_lst)/len(t_lst) == k:
                fullfilled_lst.append(t_lst)
                break
            else:
                t_lst.pop()
    t_idx = 0
    for j, lst in enumerate(fullfilled_lst):
        if len(lst) > len(fullfilled_lst[t_idx]):
            t_idx = j
    return fullfilled_lst[t_idx]


        


list_input = list(int(x) for x in input("Nhap list: ").split())
output = ex88(list_input, int(input("Nhap k: ")))
output.sort()
print(output)