import random

d = {"a": 1, "b": 2, "c": 3, "d": 4}

lst_keys = list(d.keys())
lst_vals = list(d.values())
random.shuffle(lst_keys)

print(lst_keys)
random.shuffle(lst_vals)
print(lst_vals)
new_d = dict(zip(lst_keys, lst_vals))
print(new_d)