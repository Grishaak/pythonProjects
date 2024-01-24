def order_weight(string: str):
    original_list = []
    dict_numbers = dict()
    number = ''
    for i in string:
        if i.isspace():
            original_list.append(number)
            number = ''
        else:
            number += i
    original_list.append(number)
    print(original_list)
    count = 1
    for key in original_list:
        dict_numbers[key] = (original_list.count(key), sum([int(i) for i in list(key)]))
    sorted_dict = dict(sorted(dict_numbers.items(), key=lambda x: x[1][1]))
    sub_list = list()
    result_list = list()
    start_point = 0
    end_point = 0
    values_from_dict = sorted_dict
    keys_from_dict = []
    print(sorted_dict.items())
    print(list(sorted_dict.keys()))
    for i in range(len(sorted_dict) - 1):
        if list(sorted_dict.items())[i][1][0] > 1:
            point = i
            for i in range(point, list(sorted_dict.items())[i][1][0]):
                sub_list.append(list(sorted_dict.keys())[point])
        if list(sorted_dict.items())[i][1][1] == list(sorted_dict.items())[i + 1][1][1]:
            end_point += 1
        else:
            sub_list += list(sorted_dict.keys())[start_point + 1:end_point + 1]
            start_point = i + 1
            end_point = i + 1
            sub_list.sort()
            result_list += sub_list
            print(sub_list)
            sub_list.clear()
    if (end_point + 1 == len(sorted_dict)) and (list(sorted_dict.keys())[end_point] not in sub_list):
        result_list.append(list(sorted_dict.keys())[end_point])
    return " ".join(result_list)


print(order_weight("2000 10003 11 1234000 44444444 44444444 9999 11 22 123"))
