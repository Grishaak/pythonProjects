def mix(s1: str, s2: str):
    s1 = "".join([i for i in s1 if i.isalnum() and i.islower()])
    s2 = "".join([i for i in s2 if i.isalnum() and i.islower()])
    s1_dict = {i: s1.count(i) for i in s1 if s1.count(i) > 1}
    s2_dict = {i: s2.count(i) for i in s2 if s2.count(i) > 1}
    s1 = dict(sorted(s1_dict.items(), key=lambda item: item[0]))
    s2 = dict(sorted(s2_dict.items(), key=lambda item: item[0]))
    new_list = []
    for k, v in s1.items():
        if k in s2.keys():
            if v > s2.get(k):
                new_list.append(f"1:{k * v}")
                s2.pop(k)
            elif v == s2.get(k):
                new_list.append(f"=:{k * v}")
                s2.pop(k)
            else:
                new_list.append(f"2:{k * s2.get(k)}")
                s2.pop(k)
        else:
            new_list.append(f"1:{k * v}")
    for k, v in s2.items():
        new_list.append(f"2:{k * v}")
    new_list = sorted(new_list, key=lambda item: len(item), reverse=True)
    temp_list = []
    last_list = []
    for i in range(1, len(new_list)):
        if len(new_list[i]) == len(new_list[i - 1]):
            temp_list.append(new_list[i - 1])
            if i + 1 == len(new_list):
                temp_list.append(new_list[i])
                temp_list.sort()
                for j in temp_list:
                    last_list.append(j)
                break
            if len(new_list[i]) != len(new_list[i + 1]):
                temp_list.append(new_list[i])
                temp_list.sort()
                for j in temp_list:
                    last_list.append(j)
                temp_list = []
        else:
            last_list.append(new_list[i - 1])
    last_last_list = []
    for i in last_list:
        if i not in last_last_list:
            last_last_list.append(i)
    return "/".join(last_last_list)


mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp")
