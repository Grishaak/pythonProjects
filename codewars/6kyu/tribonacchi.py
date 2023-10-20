def tribonacci(signature: list, n: int):
    for i in range(3, n):
        signature.append(sum(signature[-3:]))
    return signature[:n]



print(tribonacci([1, 1, 1], 10))
