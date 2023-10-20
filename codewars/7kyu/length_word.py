def find_short(s: str):
    return min([len(i) for i in s.split(" ")])


print(find_short("Oke y here we go"))
