def factorial_reciproco(n):
    i = 1
    prod = 1
    while i <= n:
        prod *= i
        i += 1
    return 1/prod

def signo(n):
    if n % 2 == 0:
        return 1
    else:
        return -1
