def to_jaden_case(string: str):
    return " ".join([i.capitalize() for i in string.split(" ")])


print(to_jaden_case("I am no longer alive"))
