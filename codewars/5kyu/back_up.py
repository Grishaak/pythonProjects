key_list = []
    dict_numbers = dict()
    number = ''
    for i in string:
        if i.isspace():
            key_list.append(number)
            number = ''
        else:
            number += i
    key_list.append(number)
    print(key_list)
    values_list = []
    for key in key_list:
        values_list.append(sum([int(i) for i in list(key)]))
    print(values_list)
    sorted_value_list = sorted(values_list)
    sorted_key_list = sorted(key_list)
    sub_list = list()
    result_list = list()
    start_point = 0
    end_point = 0
    print(sorted_value_list)
    print(sorted_key_list)
    for i in range(len(values_list) - 1):
        if values_list[i] == values_list[i + 1]:
            end_point += 1
        else:
            sub_list = key_list[start_point:end_point + 1]
            start_point = i + 1
            end_point = i + 1
            sub_list.sort()
            result_list += sub_list
            print(sub_list)
            sub_list.clear()
    if (end_point + 1 == len(values_list)) and (key_list[end_point] not in sub_list):
        result_list.append(key_list[end_point])
    print(result_list)