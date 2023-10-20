# Create a function that takes an integer as an argument and returns
#  "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    even_odd = ["Even", "Odd"]
    return even_odd[number % 2]


print(even_or_odd(-123))
