# Задана строка s , содержащая только символы
# '(', ')', '{' '}', '[' ']', определите, является ли введенная строка допустимой.
# Строка ввода допустима, если:
#
# Открытые скобки должны быть закрыты скобками того же типа.
# Открытые скобки должны быть закрыты в правильном порядке.
# Каждой закрывающей скобке соответствует открывающая скобка того же типа.


def isValid(s: str) -> bool:
    my_dict = {"(": ")", "{": "}", "[": "]"}
    string = ""
    for i in s:
        string += i
        if my_dict.get(i):


isValid("({[]}){[{[]}]}")
