# A, E, I, O, U.
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove
# all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.


def disemvowel(string_):
    return "".join([i for i in string_ if i.upper() not in ["A", "E", "I", "O", "U"]])


print(disemvowel("This website is for losers LOL!"))
