import math


def is_square(n):
    return n > -1 and (n ** 0.5) % 1 == 0


number = 4
print(is_square(number))
