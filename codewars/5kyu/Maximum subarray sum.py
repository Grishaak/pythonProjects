# The maximum sum subarray problem consists in
# finding the maximum sum of a contiguous subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only
# positive numbers and the maximum sum is the sum of the
# whole array. If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray
# from random import randint
#
# Not my decision below, i'm suck( --->


def max_sequence(arr):
    sub_arr = [0]
    # point where we begin our count and where we can compare digits
    max_sum = 0
    # default is zero
    for num in arr:
        sub_arr.append(max(sub_arr[len(sub_arr) - 1] + num, num))
        print(sub_arr)
        max_sum = max(max_sum, sub_arr[-1])
        print(max_sum)
    return max_sum


z = max_sequence([3, -4, 7])
print(z)
