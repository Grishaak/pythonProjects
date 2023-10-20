# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.

def find_it(seq: list):
    new_seq = {i: seq.count(i) for i in seq}
    for i in new_seq:
        if new_seq.get(i) % 2 != 0:
            return i


my_list = [1, 1, 1, 1, 3]
print(my_list)
print(find_it(my_list))
