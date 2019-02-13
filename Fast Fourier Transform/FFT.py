"""
Implementation of the forward Fourier and the inverse Fourier transform in Python to multiply two polynomials.
"""

import cmath
import math
import random


def FFT(a, flag=False):
    n = len(a)

    if n == 1:
        return a
    else:
        if flag:
            omega_n = 1 / cmath.exp((2.0 * cmath.pi * 1j) / n)
        else:
            omega_n = cmath.exp((2.0 * cmath.pi * 1j) / n)
        omega = 1
        U = FFT(a[0::2], flag)
        W = FFT(a[1::2], flag)
        V = [0] * n
        for j in range(0, n // 2):
            V[j] = U[j] + omega * W[j]
            V[j + (n // 2)] = U[j] - omega * W[j]
            omega *= omega_n
        return V


def iFFT(Z):
    a = FFT(Z, True)
    return [val / len(a) for val in a]


degree = int(input("Enter degree:"))
n = degree + 1
x = []
y = []

nearest_pow = math.ceil(math.log(degree + 1, 2))

for i in range(0, n):
    x.append(random.randint(1, 5))
    y.append(random.randint(1, 5))

for i in range(0, pow(2, nearest_pow) - n):
    x.append(0)
    y.append(0)

n += pow(2, nearest_pow) - n

for i in range(0, pow(2, nearest_pow)):
    x.append(0)
    y.append(0)

n *= 2

print("coefficients of x:", x)
print("coefficients of y:", y)
print("n:", n)
X = FFT(x)
print("\nFast Fourier Transform(x):", X)
Y = FFT(y)
print("\nFast Fourier Transform(y):", Y)

Z = []
for i in range(0, n):
    Z.append(X[i] * Y[i])
print("\nZ:", Z)

ifft_lst = ["{:.2f}".format(element) for element in iFFT(Z)]
print("\niFFT(Z):", ifft_lst)
