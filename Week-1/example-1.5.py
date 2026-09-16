import random

array = [] 
min =0
max = 20

n = 5

for i in range(0, n):
    num = random.randint(min, max)
    array.append(num)

print(array)