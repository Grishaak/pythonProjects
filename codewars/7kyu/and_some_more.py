def accum(s):
    return "-".join([str(char * i).capitalize() for i, char in enumerate(s, 1)])


print(accum("ZpglnRxqenU"))
