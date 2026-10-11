import random

def random_array(size):
    return [random.randint(0, 99) for _ in range(size)]

print(random_array(5))

