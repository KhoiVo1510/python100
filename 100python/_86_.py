white_space = [' ']
class Food():
    def __init__(self):
        self.chicken = 30000
        self.ham = 25000
        self.coke = 10000
    
    def get_order(self):
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
    def __str__(self):
        return f"Chào mừng các bạn đến với nhà hàng thức ăn nhanh!\nMời bạn nhập số lượng từng món ăn:\n"
        
food = Food()
print(food)
food.get_order()
food.cal_price()