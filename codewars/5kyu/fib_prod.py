def productFib(prod):
    x, y = 0, 1
    count = 0
    while True:
        count += 1
        z = x + y
        if x * y == prod:
            return [x, y, True]
        if x * y > prod:
            return [x, y, False]
        x, y = y, z


# def find_fib(num, prod):
#     x, y = 0, 1
#     for i in range(num):
#         z = x + y
#         if x * y == prod:
#             return True
#         x = y
#         y = z
#     return x


print(productFib(800))
