class Check():
    def __init__(self):
        self.WAIT = int(input("Wait: ")) + 1
        self.wait = self.WAIT
        self.count, self.a, self.b = 0, 0, 0
        self.valid = "Wait"
        self.sequence = []

    def my_append(self, N):
        self.valid = self.check_valid(N)
        if self.count == 0:
            self.a = N
            self.count += 1
        elif self.count == 1:
            self.b = N
            self.count += 1
        else:
            self.a, self.b = self.b, N
        self.sequence.append(N)

    def check_valid(self, N):
        if self.wait > 1:
            self.wait -= 1
            return "Wait"
        elif self.wait == 1:
            self.wait -= 1
            return "Pass"
        if N == self.a:
            self.wait = self.WAIT
            return "Failed"
        return "Pass"

if __name__ == "__main__":
    sequence_t = Check()
    while True:
        inp = int(input("next: "))
        if inp != 0 and inp != 1:
            break
        sequence_t.my_append(inp)
        print(f"Current sequence: {sequence_t.sequence}")
        print(f"Lastest bit validation: {sequence_t.valid}")