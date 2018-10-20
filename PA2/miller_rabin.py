import random


def isPrime(n, k):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False

    x = n - 1
    r = 1
    d = 0
    while True:
        d = x // 2 ** r
        if d % 2 == 1:
            break
        else:
            r += 1

    for i in range(1, k + 1):
        if not miller_rabin(n, d, r):
            return False

    return True


def miller_rabin(n, d, r):
    a = random.randint(2, n - 2)
    x = (a ** d) % n

    if x == 1 or x == n - 1:
        return True

    for i in range(1, r):
        x = (x ** 2) % n
        if x == 1:
            return False
        if x == n - 1:
            return True
