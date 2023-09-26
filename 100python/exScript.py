import main 
import run
import math
import calendar
import random

def my_replace(old_str = str, *args):
    for delimiter in args:
        new_str = old_str.replace(delimiter, '', 1)
    return new_str

def check_prime_number(n = int):
    if n < 2:
        return False
    if n == 2:
        return True
    for num in range(2, int(math.sqrt(n)) + 1):
        if n%num == 0:
            return False
    return True

def genfibonacci(n = int):
    a = 1
    b = 1
    while a < n:
        yield a
        a, b = b, a + b

class Ex_01():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            n = (input("Enter the variable: n = "))
            if my_replace(n, '.', '-').isdigit():
                output = (float(n)*3) + 1
                print ("===> Output: ", output)
                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Nhập vào số n, hãy nhân n lên cho 3,
rồi cộng 1 sau đó in kết quả ra màn hình
"""

class Ex_02():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            n = (input("Enter the variable: n = "))
            if my_replace(n, '.', '-').isdigit():
                output = (float(n)**2)/3
                print ("===> Output: ", output)
                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Nhập vào số n, hãy mũ 2 rồi chia cho 3,
sau đó in kết quả ra màn hình
"""

class Ex_06():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            a = (input("Enter the variable: a = "))
            if my_replace(a, '-').isdigit():
                a = int(a)
                output = (a % 5 == 0) and ((a < 20) or (a > 70))
                print ("===> Output: ", output)
                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm
trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
"""

class Ex_16():
    def __init__(self):
        print(self)
        self.lst = [0]*3
        while True:
            print("Nhập độ dài 3 cạnh của tam giác: ")
            lst = [input("a = "), input("b = "), input("c = ")]
            typo = False
            for num in lst:
                if not(my_replace(num, '.').isdigit()):
                    typo = True
            if not(typo):
                break
            print("Type again.\n")
        
        self.lst = lst
    def execute(self):
        a = float(self.lst[0])
        b = float(self.lst[1])
        c = float(self.lst[2])

        if not((a > abs(b-c)) and (a < (b+c))\
    and (b > abs(a-c)) and (b < (a+c))\
    and (c > abs(a-b)) and (c < (a+b))):
            print("===> Output: Đây không phải là tam giác.")
        else:
            if len(set(self.lst)) == 1:
                print("===> Output: Đây là tam giác đều.")

            elif len(set(self.lst)) == 2:
                if 2*(a**2) == c**2:
                    print("===> Output: Đây là tam giác vuông cân.")
                else:
                    print("===> Output: Đây là tam giác cân.")

            else:
                if a**2 + b**2 == c**2:
                    print("===> Output: Đây là tam giác vuông.")
                else:
                    print("===> Output: Đây là tam giác thường.")

    def __str__(self):
        return """
(?) Nhập vào 3 số thực dương a, b, c.
Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không?
nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì
(tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
"""

class Ex_21():
    def __init__(self):
        print(self)
        self.date = [0]*2
        tmp_c = calendar.Calendar()
        while True:
            lst = [input("Nhập ngày: "), input("Nhập tháng: ")]
            typo = False
            date_valid = False
            for num in lst:
                if not(num.isdigit()):
                    typo = True
            if not(typo) and 0 < (int(lst[1]) <= 12) and (int(lst[0]) != 0):
                days_in_month = list(tmp_c.itermonthdays(2023, int(lst[1])))
                if int(lst[0]) in days_in_month:
                    date_valid = True
            if date_valid:
                break                
            print("Type again.\n")
        self.date = lst
        del tmp_c
    
    def execute(self):
        tmp_c = calendar.Calendar()
        self.total_days = -1
        d = int(self.date[0])
        m = int(self.date[1])

        for i in range(1, m):
            self.total_days += max(tmp_c.itermonthdays(2023,i))
        self.total_days += d

        print(f"===> Output: {self.total_days} days")


    def __str__(self):
        return """
(?) Nhập vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày
đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận).
"""

class Ex_27():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            h = (input("Nhập chiều cao tam giác: h = "))
            if h.isdigit():
                h = int(h)
                print ("===> Output: ")
                for a in range(h):
                    if a == 0:
                        print(f"{' '*(h-1-a)}*")
                        continue
                    if a == (h-1):
                        print(f"{'*'*(2*h-1)}")
                        continue
                    print(f"{' '*(h-1-a)}*{' '*(2*a-1)}*")
                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím.
"""

class Ex_32():
    def __init__(self):
        print(self)
        self.a = [0, []]
        self.b = [0, []]
        while True:
            a = input("Nhập a: ")
            b = input("Nhập b: ")
            if a.isdigit() and b.isdigit():
                self.a[0] = int(a)
                self.b[0] = int(b)
                break
            print("Type again.\n")
    def execute(self):
        for num in range(1, self.a[0]):
            if self.a[0]%num == 0:
                self.a[1].append(num)
        for num in range(1, self.b[0]):
            if self.b[0]%num == 0:
                self.b[1].append(num)
        print ("===> Output: ")
        print(f"Ước của a: {self.a[1]}.")
        print(f"Ước của b: {self.b[1]}.")
        uc = set(self.a[1]).intersection(set(self.b[1]))
        print(f"Ước chung lớn nhất của a và b: {max(uc)}")

    def __str__(self):
        return """
(?) Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b,
in ra UCLN của a và b
"""

class Ex_33():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            a = (input("Nhập số nguyên dương a = "))
            if a.isdigit():
                print ("===> Output: ")
                if check_prime_number(int(a)):
                    print(f"{int(a)} là số nguyên tố.")
                    break
                print(f"{int(a)} không phải là số nguyên tố.")
                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không?
"""

class Ex_40():
    def __init__(self):
        print(self)

    def execute(self):
        while True:
            n = input("Nhập số nguyên dương n: ")
            if n.isdigit():
                n = int(n)
                all_digit = []
                while(n >= 1):
                    all_digit.append(n%10)
                    n //= 10
                print(f"Các chữ số có trong n: {set(all_digit)}")
                even_digit = set(filter(lambda num: num%2 == 0, all_digit))
                odd_digit = set(filter(lambda num: num%2 == 1, all_digit))
                
                print ("===> Output: ")
                print(f"Các chữ số chẵn trong n: {even_digit}")
                print(f"Các chữ số lẻ trong n: {odd_digit}")
                print(f"Tổng các chữ số trong n: {sum(all_digit)}")

                break
            print("Type again.\n")

    def __str__(self):
        return """
(?) Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn,
bao nhiêu chữ số lẻ, tính tổng các chữ số của n
"""

class Ex_42():
    def __init__(self):
        print(self)

    def execute(self):
        a = input("Nhập vào A: ")
        if a.isdigit():
            a = int(a)
            lst = []
            for num in genfibonacci(a):
                lst.append(num)
            print ("===> Output: ")
            print(f"Dãy fibonacci: {lst}")
            print(f"Số lớn nhất trong dãy: {max(lst)}")
        pass

    def __str__(self):
        return """
(?) Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,...
với số kế tiếp sẽ bằng tổng hai số trước đó.
Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
"""
    
class Ex_49():
    def __init__(self):
        print(self)

    def execute(self):
        _str = input("Nhập chuỗi: ")

        result_1 = 0
        for let in _str:
            if let.isdigit():
                result_1 += int(let)

        result_2 = 0
        newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in _str)
        num_list = [int(i) for i in newstr.split()]
        for num in num_list:
            result_2 += num
        print("===> Output: ")
        print(f"Tổng giá trị ký tự số trong chuỗi = {result_1}")
        print(f"Tổng giá trị các con số trong chuỗi = {result_2}")

    def __str__(self):
        return """
(?) Nhập vào một chuỗi:
- hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
- hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng.
"""

class Ex_52():
    def __init__(self):
        print(self)

    def execute(self):
        s1 = input("Nhập vào chuỗi a: ")
        s2 = input("Nhập vào chuỗi b: ")
        index = s1.find(s2)
        if index == -1:
            print("Không có chuỗi b trong chuỗi a.")
        else:
            s1 = s1[:index] + s1[index + len(s2):]
            print("===> Output: ", s1)

    def __str__(self):
        return """
(?)Nhập vào chuỗi a và chuỗi b
Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)"""

class Ex_68():
    def __init__(self):
        print(self)
        typo = True
        while typo:
            try:
                self.lst = list(int(x) for x in input("Nhập list: ").split())
                typo = False
            except Exception as e:
                print(f"Error(s) occur.\n{e}\nType again.\n")

    def execute(self):
        lst = self.lst
        result_1 = [lst[0]]

        for i in range(1, len(lst)):
            if lst[i] > result_1[-1]:
                result_1.append(lst[i])

        even, odd, zero = [], [], []
        for num in lst:
            if num == 0:
                zero.append(num)
            elif num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        max_i = lst.index(max(lst))
        min_i = lst.index(min(lst))
        lst[max_i], lst[min_i] = lst[min_i], lst[max_i]

        print(f"===> Output 1: {result_1}")
        print(f"===> Output 2: {list(even + zero + odd)}")
        print(f"===> Output 3: {lst}")
        

    def __str__(self):
        return """
(?) Nhập vào một list số nguyên L:
- hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó
- hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
- hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất"""

class Ex_80():
    def __init__(self):
        print(self)
        typo = True
        while typo:
            try:
                self.lst = list(int(x) for x in input("Nhập list: ").split())
                self.a = int(input("Nhập a: "))
                typo = False
            except Exception as e:
                print(f"Error(s) occur.\n{e}\nType again.\n")

    def execute(self):
        def create_prime_num_list(L, a):
            prime_list = []
            for num in L:
                if check_prime_number(num):
                    prime_list.append(num)
            if len(prime_list) > a:
                prime_list = prime_list[0:a]
            elif 0 < len(prime_list) < a:
                while(len(prime_list) < a):
                    prime_list.append(prime_list[-1])
            return prime_list

        list_output = create_prime_num_list(self.lst, self.a)
        
        if not(len(list_output)):
            print("===> Output: Không có số nguyên tố trong list")
        else:
            print(f"===> Output: {list_output}")

    def __str__(self):
        return """
(?) Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và
trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L"""
    
class Ex_81():
    def __init__(self):
        print(self)
        typo = True
        while typo:
            try:
                self.lst = list(int(x) for x in input("Nhập list: ").split())
                self.a = int(input("Nhập a: "))
                if self.a < len(self.lst):
                    typo = False
                else:
                    print("Type again.")
            except Exception as e:
                print(f"Error(s) occur.\n{e}\nType again.\n")

    def execute(self):
        def return_nth_value(L, a):
            L.sort()
            return_value = L[a]
            cnt = L.count(return_value)
            return (return_value, cnt)

        output = return_nth_value(self.lst, self.a)

        print(f"Có {output[1]} giá trị lớn thứ {self.a} trong list: {output[0]}.")

    def __str__(self):
        return """
(?) Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và
trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất, a = 2
thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)
"""

class Ex_85():
    def __init__(self):
        print(self)

    def execute(self):
        def shuffle_dictionary(d):
            lst_keys = list(d.keys())
            lst_vals = list(d.values())

            random.shuffle(lst_keys)
            random.shuffle(lst_vals)
            
            shuffled_d = dict(zip(lst_keys, lst_vals))
            rev_multidict = {}
            for key, value in shuffled_d.items():
                rev_multidict.setdefault(value, set()).add(key)
            if len([key for key, values in rev_multidict.items() if len(values) > 1]) != 0:
                return None
            return shuffled_d
         
        d_input = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 1}
        d_output = shuffle_dictionary(d_input)

        print("===> Input: ", d_input)
        print("===> Output: ", d_output)


    def __str__(self):
        return """
(?) Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary
mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary
mới đó. Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào
có 2 giá trị trùng nhau), hàm trả về None
"""

class Ex_86():
    def __init__(self):
        print(self)
        self.chicken = 30000
        self.ham = 25000
        self.coke = 10000
    
    def get_order(self):
        print(f"{'-'*20}")
        print("""
Chào mừng các bạn đến với nhà hàng thức ăn nhanh!
Mời bạn nhập số lượng từng món ăn:""")

        self.n_chicken = int(input("Gà rán: "))
        self.n_ham = int(input("Hamburger: "))
        self.n_coke = int(input("Cocacola: "))
        print("\nHóa đơn:")
        t_str = f'{self.chicken:,}'.replace(',', '.')
        print(f"Gà rán{' '*14}{t_str}đ x {self.n_chicken}")
        t_str = f'{self.ham:,}'.replace(',', '.')
        print(f"Hamburger{' '*11}{t_str}đ x {self.n_ham}")
        t_str = f'{self.coke:,}'.replace(',', '.')
        print(f"Cocacola{' '*12}{t_str}đ x {self.n_coke}")

    def cal_price(self):
        self.p_chicken = self.chicken * self.n_chicken
        self.p_ham = self.ham * self.n_ham
        self.p_coke = self.coke * self.n_coke
        print("\nTổng:")
        t_str = f'{self.p_chicken:,}'.replace(',', '.')
        print(f"Gà rán{' '*14}{t_str}đ")

        t_str = f'{self.p_ham:,}'.replace(',', '.')
        print(f"Hamburger{' '*11}{t_str}đ")
        
        t_str = f'{self.p_coke:,}'.replace(',', '.')
        print(f"Cocacola{' '*12}{t_str}đ")

        self.total = self.p_chicken + self.p_ham + self.p_coke
        t_str = f'{self.total:,}'.replace(',','.')
        print(f"Tổng trước thuế{' '*5}{t_str}đ")

        self.tax = self.total * (5/100)
        t_str = f'{self.tax:,}'.replace(',','.')
        print(f"Thuế (5%){' '*11}{t_str}đ")
        
        t_str = f'{self.total - self.tax:,}'.replace(',','.')
        print(f"Tổng sau thuế{' '*7}{t_str}đ")

        print(f"{'-'*20}")

    def execute(self):
        self.get_order()
        self.cal_price()

    def __str__(self):
        return """
(?) Một nhà hàng có các món ăn:
Gà rán, hamburger, cocacola
- Giá của gà rán là: 30.000đ
- Giá của hamburger là: 25.000đ
- Giá của cocacola là: 10.000đ
Yêu cầu người dùng nhập vào số lượng từng món ăn.
Sau đó in ra hóa đơn.
"""
    
class Ex_87():
    def __init__(self):
        print(self)
        typo = True
        while typo:
            try:
                self.lst = list(int(x) for x in input("Nhập list: ").split())
                self.k = int(input("Nhập k: "))
                if self.k < len(self.lst):
                    typo = False
                else:
                    print("Type again.")
            except Exception as e:
                print(f"Error(s) occur.\n{e}\nType again.\n")

    def execute(self):
        def check_return(L, k):
            s = set(L)
            d = {item:L.count(item) for item in s}
            d = sorted(d.items(), key = lambda x: x[1])
            while(d[0][1] <= k):
                d.pop(0)
                if len(d) == 0:
                    return []
            return [x for x,y in d]
        output = check_return(self.lst, self.k)
        if len(output):
            print("===> Output: ", output)
        else:
            print("===> Output: Không có giá trị thỏa mãn.")

    def __str__(self):
        return """
Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên
dương k. Hãy tạo và trả về một list L_kq có các phần tử là giá trị của
phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần.
"""
    
class Ex_88():
    def __init__(self):
        print(self)
        typo = True
        while typo:
            try:
                self.lst = list(int(x) for x in input("Nhập list: ").split())
                self.k = int(input("Nhập k: "))
                if self.k < len(self.lst):
                    typo = False
                else:
                    print("Type again.")
            except Exception as e:
                print(f"Error(s) occur.\n{e}\nType again.\n")

    def execute(self):
        def ex88(L, k):
            fullfilled_lst = []
            for i in range(len(L)):
                t_lst = L[i:len(L)]
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
        output = ex88(self.lst, self.k)
        print(f"==> Output: ", output)
        pass

    def __str__(self):
        return """
Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên
dương k. Tìm và trả về đoạn list dài nhất trong L có giá trị trung bình là k
"""
    
class Ex_():
    def __init__(self):
        print(self)

    def execute(self):
        pass

    def __str__(self):
        return "\n\n"
if __name__ == "__main__":
    main.clearScreen()
    main.runEx()