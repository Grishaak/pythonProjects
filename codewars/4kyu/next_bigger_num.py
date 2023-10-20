from copy import deepcopy
from itertools import permutations


def next_bigger(n: int):
    my_list = [int(i) for i in str(n)]
    print(my_list)
    new_list = list(set(list(str(n))))
    if (n < 10) or 1 == new_list or int("".join(sorted([i for i in str(n)], reverse=True))) == n:
        return -1
    stop_point = 0
    for i in range(len(my_list) - 1):
        if my_list[i] <= my_list[i + 1] or i == 0:
            stop_point += 1
        else:
            break
    rest_list = my_list[:stop_point + 1]
    x_list = deepcopy(my_list)
    my_list = my_list[stop_point + 1:]
    if len(my_list) == 1:
        my_list = x_list[-3:]
        rest_list = rest_list[:-1]
    print(my_list)
    smth = sorted(list(set([''.join(p) for p in permutations("".join([str(i) for i in my_list]))])))
    print(smth)
    find = smth[smth.index("".join([str(i) for i in my_list]))]
    # print(find)
    x = int("".join([str(i) for i in rest_list]) + find)
    # print(int(x))
    # print(smth)
    # n_list = [int("".join(i)) for i in sorted(list(set(permutations(sorted([i for i in str(n)]), ))))]
    # result = n_list[n_list.index(n) + 1]
    return x


x = next_bigger(1234567890)
print(x)

# my_list = [7, 1, 4, 7, 8, 3, 1, 2, 3, 0, 5, 1]
# stop_point = 0
# for i in range(len(my_list) - 1):
#     if my_list[i] <= my_list[i + 1] or i == 0:
#         stop_point += 1
#     else:
#         break
# rest_list = my_list[:stop_point + 1]
# my_list = my_list[stop_point + 1:]
# print(sorted(list(set([''.join(p) for p in permutations("".join([str(i) for i in my_list]))]))))
# smth = sorted(list(set([''.join(p) for p in permutations("".join([str(i) for i in my_list]))])))
# find = smth[smth.index("".join([str(i) for i in my_list])) + 1]
# print(find)
# x = "".join([str(i) for i in rest_list]) + find
# print(int(x))
# print(smth)
