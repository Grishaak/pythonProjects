def rot13(message: str):
    rot13_dict = {"A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U",
                  "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A", "O": "B", "P": "C", "Q": "D",
                  "R": "E", "S": "F", "T": "G", "U": "H", "V": "I", "W": "J", "X": "K", "Y": "L", "Z": "M"}
    other_message = []
    for i in message:
        if i.upper() in rot13_dict.keys():
            if i.islower():
                other_message.append(rot13_dict.get(i.upper()).lower())
            elif i.isupper():
                other_message.append(rot13_dict.get(i.upper()))
        else:
            other_message.append(i)

    return "".join(other_message)


print(rot13("HElloПривет 124 23 Aa Bb Zz "))
