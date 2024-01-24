# Write an algorithm that takes an
# array and moves all of the zeros
# to the end, preserving the order
# of the other elements.


def move_zeros(lst: list):
    zeroes = lst.count(0)
    lst = [i for i in lst if i]
    zeroes_2 = [0 for i in range(zeroes)]
    # return sorted(list, key=lambda x: x == 0 and type(x) is not bool)
    return [i for i in lst if i] + [0 for i in range(lst.count(0))]


print(move_zeros([0, 100, 2, 1, 2, 3, 4, 0, 6, 0, 7, 0, 0, 5, 4, 2]))
