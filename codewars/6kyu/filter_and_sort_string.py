# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9.
# So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will
# only contain valid consecutive numbers.


def order(sentence: str):
    # my_dict = {}
    # for i in sentence.split():
    #     for j in i:
    #         if j.isdigit():
    #             my_dict[j] = i
    # my_dict = dict(sorted(my_dict.items()))
    # return " ".join(my_dict.values())
    return " ".join(sorted(sentence.split(), key=min))


print(order("is2 Thi1s T4est 3a"))
