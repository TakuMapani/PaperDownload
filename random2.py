import random

list=[]
for i in range(7):
    r = random.randint(1,45)
    if r not in list: list.append(r)

print(list)