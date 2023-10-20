def snail(arr: list[list[int]]):
    new_arr = []
    while len(arr):
        new_arr += arr.pop(0)
        if len(arr) == 0:
            return new_arr
        for i in range(len(arr)):
            new_arr.append(arr[i].pop())
        if len(arr) == 0:
            return new_arr
        new_arr += reversed(arr.pop())
        if len(arr) == 0:
            return new_arr
        for i in range(len(arr) - 1, 0, -1):
            new_arr.append(arr[i].pop(0))
        if len(arr) == 0:
            return new_arr
    return new_arr


print(snail([[1],
             [4, 5, 6, 101],
             [7, 8, 9],
             [10, 11, 12, 103]]))
