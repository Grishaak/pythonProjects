def rgb(r: int, g: int, b: int):
    # n = [0 if i < 0 else str(hex(i)).upper()[2:] if len(str(hex(i)).upper()[2:]) > 1 else "0" + str(hex(i)).upper()[2:]
    # if i > 255 else "FF"
    #     for i in [r, g, b]]
    n = []
    for i in [r, g, b]:
        if i < 0:
            i = 0
        if i > 255:
            i = 255
        result = str(hex(i)).upper()[2:]
        n.append(result if len(result) > 1 else "0" + result)
    return "".join(n)


print(rgb(0, 12, 12))
