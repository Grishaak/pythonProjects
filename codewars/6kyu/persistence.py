import numpy as np


# def persistence(n: int):
#     count = 0
#     while len(str(n)) != 1:
#         temp = 1
#         for i in str(n):
#             temp *= int(i)
#         n = temp
#         count += 1
#     return count


def persistence_num(n: int):
    count = 0
    while len(str(n)) != 1:
        n = str(np.prod([int(i) for i in str(n)]))
        count += 1
    return count


print(persistence_num(39))
