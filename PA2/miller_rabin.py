import random


def isPrime(n, k=11):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False

    x = n - 1
    r = 0

    while x % 2 == 0:
        x = x // 2
        r += 1

    for i in range(1, k + 1):
        if not miller_rabin(n, x, r):
            return False

    return True


def miller_rabin(n, d, r):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    for i in range(1, r):
        x = pow(x, 2, n)
        if x == n - 1:
            return True


while True:
    n = int(input("Enter No:"))
    print(isPrime(n))
