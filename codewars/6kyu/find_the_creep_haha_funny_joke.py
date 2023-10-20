# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers.
# The array is either entirely comprised of odd
# integers or entirely comprised of even integers
# except for a single integer N.
# Write a method that takes the array
# as an argument and returns this "outlier" N.

def find_outlier(integers):
    odd = []
    even = []
    count = 0
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        count += 1
        if count > 3 and ((len(odd) != 0) and (len(even) != 0)):
            if len(odd) > len(even):
                return even.pop()
            elif len(odd) < len(even):
                return odd.pop()


print(find_outlier([2, 2, 2, 2, 4, 5]))
