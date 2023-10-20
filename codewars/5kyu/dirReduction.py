def dirReduc(arr: list[str]):
    index_list = []
    new_arr = []
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if (arr[i] == 'NORTH') and (arr[i + 1] == 'SOUTH'):
                index_list.append(i)
                index_list.append(i + 1)
            elif (arr[i] == "SOUTH") and (arr[i + 1] == "NORTH"):
                index_list.append(i)
                index_list.append(i + 1)
            elif (arr[i] == "WEST") and (arr[i + 1] == "EAST"):
                index_list.append(i)
                index_list.append(i + 1)
            elif (arr[i] == "EAST") and (arr[i + 1] == "WEST"):
                index_list.append(i)
                index_list.append(i + 1)
        new_list_ind = []
        for i in range(len(index_list)):
            if index_list.count(index_list[i]) == 1:
                new_list_ind.append(index_list[i - 1])
        print(new_list_ind)
        index_list = new_list_ind.copy()
        print(index_list)
        print(arr)
        if len(index_list) > 0:
            flag = True
        for j in range(len(arr)):
            if j not in index_list:
                # print(arr[j])
                new_arr.append(arr[j])
        print(new_arr)
        index_list = []
        arr = new_arr.copy()
        new_arr = []
    return arr


print(dirReduc(
    ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']))
