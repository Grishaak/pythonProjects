def bool_to_word(boolean):
    return {True: "Yes", False: "No"}.pop(boolean)


print(bool_to_word(True))
