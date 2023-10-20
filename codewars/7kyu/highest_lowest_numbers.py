# In this little assignment you are given a string of space
# separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers: str):
    numbers = [int(i) for i in numbers.split(' ')]
    return f"{max(numbers)} "f"{min(numbers)}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
