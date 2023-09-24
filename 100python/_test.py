import time

def draw_triangle(h):
    for a in range(h):
        if a == 0:
            print(f"{' '*(h-1-a)}*")
        elif a == (h-1):
            print(f"{'*'*(2*h-1)}")
        else:
            print(f"{' '*(h-1-a)}*{' '*(2*a-1)}*")

h = input("Nhap chieu cao: ")
start = time.time()
if h.isdigit():
    draw_triangle(int(h))
else:
    print("type again.")

run_time = time.time() - start
print(run_time)