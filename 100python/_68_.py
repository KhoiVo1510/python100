def ex66(lst):
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > result[-1]:
            result.append(lst[i])
    return result


def ex67(lst):
    even = []
    odd = []
    zero = []
    for num in lst:
        if num == 0:
            zero.append(num)
        elif num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return (even + zero + odd)

def ex68(lst):
    max_i = lst.index(max(lst))
    min_i = lst.index(min(lst))
    lst[max_i], lst[min_i] = lst[min_i], lst[max_i]

    return lst

list_input = list(int(x) for x in input("Nhap list: ").split())
print(list(ex66(list_input)))
print(list(ex67(list_input)))
print(list(ex68(list_input)))


# ex67(list_input)
# ex68(list_input)