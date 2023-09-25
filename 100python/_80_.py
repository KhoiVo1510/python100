import math

def check_prime_num(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for num in range(2, int(math.sqrt(n)) + 1):
        if n%num == 0:
            return False
    return True

def create_prime_num_list(L, a):
    prime_list = []
    for num in L:
        if check_prime_num(num):
            prime_list.append(num)
    if len(prime_list) > a:
        prime_list = prime_list[0:a]
    elif 0 < len(prime_list) < a:
        while(len(prime_list) < a):
            prime_list.append(prime_list[-1])
    return prime_list
    
list_input = list(int(x) for x in input("Nhap list: ").split())

list_output = create_prime_num_list(list_input, int(input("Nhap a: ")))

if not(len(list_output)):
    print("Khong co so nguyen to trong list.")
else:
    print(list_output)
