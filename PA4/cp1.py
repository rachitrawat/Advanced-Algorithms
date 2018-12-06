import math
from _operator import itemgetter


def dist(p1, p2):
    return pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)


def bruteForce(P, n):
    min_ = dist(P[0], P[1])
    pair = [P[0], P[1]]
    for i in range(0, n):
        for j in range(i + 1, n):
            d = dist(P[i], P[j])
            if d < min_:
                min_ = d
                pair = [P[i], P[j]]
    return math.sqrt(min_), pair


def closestStrip(strip, size, d):
    min_ = pow(d, 2)
    strip = sorted(strip, key=itemgetter(1))
    pair = []
    for i in range(0, size):
        for j in range(i + 1, min(size, i + 6)):
            if abs(strip[j][1] - strip[i][1]) < min_:
                d = dist(strip[i], strip[j])
                if d < min_:
                    min_ = d
                    pair = [strip[i], strip[j]]
    return math.sqrt(min_), pair


def closestPair(P, n):
    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    midpt = P[mid]

    dL, pairL = closestPair(P[0:mid:1], mid)
    dR, pairR = closestPair(P[mid:n:1], n - mid)
    d = min(dL, dR)

    if d == dL:
        pair = pairL
    else:
        pair = pairR

    strip = []
    for i in range(0, n):
        if abs(P[i][0] - midpt[0]) < d:
            strip.append(P[i])

    dStrip, pairStrip = closestStrip(strip, len(strip), d)
    dFinal = min(d, dStrip)

    if dFinal == d:
        return dFinal, pair
    else:
        return dStrip, pairStrip


def main(P, n):
    P = sorted(P, key=itemgetter(0))
    return closestPair(P, n)


P = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
distance, pair = main(P, len(P))
distance = "%.2f" % distance
print("Closest pair: %s Distance: %s" % (pair, distance))

import matplotlib.pyplot as plt

plt.figure()

for point in P:
    plt.plot([point[0]], [point[1]], marker='o', markersize=4, color="black")

plt.plot([pair[0][0]], [pair[0][1]], marker='o', markersize=4, color="red")
plt.plot([pair[1][0]], [pair[1][1]], marker='o', markersize=4, color="red")

plt.show()
