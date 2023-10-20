def create_phone_number(n):
    # return f"({''.join([str(i) for i in n[:3]])}) " \
    #                + f"{''.join([str(i) for i in n[3:6]])}-" \
    #                + f"{''.join([str(i) for i in n[6:]])}"
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
