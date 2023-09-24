#Ex 38 39 40 
def get_all_digit(n):
    if not(n.isdigit()):
        return False
    n = int(n)
    result = []
    while(n >= 1):
        result.append(n%10)
        n = n//10
    return result
n = input("Nhap so nguyen duong n: ")

result = (get_all_digit(n))
print(f"Cac chu so trong n: {set(result)}")
result_even = set(filter(lambda num: num%2 == 0, result))
result_odd = set(filter(lambda num: num%2 == 1, result))

print(f"Cac chu so chan trong n: {result_even}")
print(f"Cac chu so le trong n: {result_odd}")
print(f"Tong cac chu so trong n: {sum(result)}")