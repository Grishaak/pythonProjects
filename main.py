# def comp(array1, array2):
#     print(array1)
#     print(array2)
#     if (None == array1) or (None == array2):
#         return False
#     if not array1:
#         if not array2:
#             return True
#         else:
#             return False
#     for i in range(len(array1)):
#         if array1[i] < 0:
#             array1[i] = -array1[i]
#     for i in range(len(array2)):
#         if array2[i] < 0:
#             array2[i] = -array2[i]
#     array1.sort()
#     array2.sort()
#     for i in range(len(array1)):
#         if array1[i] * array1[i] == array2[i]:
#             pass
#         else:
#             return False
#     return True
#
#
# x = []
# y = []
# print(comp(x, y))


x = [[0, 0]]*2
print(x)
y = x
y[1][1] = 1
print(x)