s1 = input("Nhap vao chuoi a: ")
s2 = input("Nhap vao chuoi b: ")
index = s1.find(s2)
s1 = s1[:index] + s1[index + len(s2):]
print(s1)