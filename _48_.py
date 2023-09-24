def tongsotrongchuoi(s):
    result = 0
    for let in s:
        if let.isdigit():
            result += int(let)
    return result

def tongconsotrongchuoi(s):
    result = 0
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in s)
    print(newstr)
    num_list = [int(i) for i in newstr.split()]
    for num in num_list:
        result += num
    return result

_str = input("Nhap chuoi s: ")
print(tongsotrongchuoi(_str))
print
print(tongconsotrongchuoi(_str))