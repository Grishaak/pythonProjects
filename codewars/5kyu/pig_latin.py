# Move the first letter of each word to
# the end of it, then add "ay" to the
# end of the word. Leave punctuation marks untouched.


def pig_it(text: str):
    # when import re
    # return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.
    return " ".join([i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split(" ")])


print(pig_it("Pig latin is cool ? "))
