import re


def first_non_repeating_letter(s: str):
    for i in s:
        if s.lower().count(i.lower()) == 1:
            return i
    return ''


def parse_easy_way(s: str) -> str:
    print('Original string: ', s)
    # initialize punc pattern
    punc = r"""(\!()-[]{}:;'",<>./?@#$%^&*_~)"""
    for i in s:
        # search for pattern in string
        if i in punc:
            s = s.replace(i, '')
    return s


def parse_with_re(s: str):
    import re

    # initializing string
    # test_str = "Gfg, is best : for ! Geeks ;"

    # printing original string
    print("The original string is : " + s)

    # Removing punctuations in string
    # Using regex
    res = re.sub(r'[^\w\s]', '', s)
    return res


def parse_with_filter(s: str):
    # Using filter() and lambda function to filter out punctuation characters
    print(s)
    result = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), s))
    return result


print(first_non_repeating_letter('sTressS'))

# print(f"Parsed with easy_way string:\n",parse_easy_way(r"Today is (a \G)/oo#%d d#ay^! Sir, H]ow ar[e yo>u?"),"\n")
# print(f"Parsed with regex string:\n",parse_with_re(r"Today is (a \G)/oo#%d d#ay^! Sir, H]ow ar[e yo>u?"),"\n")
# print(f"Parsed with filter string:\n",parse_with_filter(r"Today is (a \G)/oo#%d d#ay^! Sir, H]ow ar[e yo>u?"))
