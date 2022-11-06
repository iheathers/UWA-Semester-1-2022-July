def power(x, N):
    return x ** N


def power2(x, N):
    prod = 1

    for i in range(N):
        prod = prod * x

    return prod


def power3(x, N):
    if N <= 1:
        return x
    if N % 2 == 0:
        return power3(x, N // 2) * power3(x, N // 2)
    else:
        return x * power3(x, N // 2) * power3(x, N // 2)


print(power(3, 1001))
print(power2(3, 1001))
print(power3(3, 3))
