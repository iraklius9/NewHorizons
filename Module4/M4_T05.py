import math


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")
print()
