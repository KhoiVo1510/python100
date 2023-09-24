def genfibonacci(n):
    a = 1
    b = 1
    while a < n:
        yield a
        a, b = b, a + b
def get_fibonacci_list(n):
    if not(n.isdigit()):
        return False
    n = int(n)
    result = []
    for num in genfibonacci(int(a)):
        result.append(num)
    return result
a = input("Nhap A: ")
result = get_fibonacci_list(a)
if not(result):
    print("Type Again.")
else:
    print(f"Day so fibonacci: {result}")
    print(f"So lon nhat trong day: {max(result)}")