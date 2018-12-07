from random import shuffle

from PA4.modules import utils


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return val


def GrahamScan(P, n):
    P = utils.simple_polygon(P)
    hull = []

    max_x = max([item[0] for item in P])
    min_y = min([item[1] for item in P if item[0] == max_x])
    extreme_pt = [max_x, min_y]
    print("Extreme point:", extreme_pt)

    hull.append(P[0])
    hull.append(P[1])
    hull.append(P[2])

    for i in range(3, n):
        while not orientation(hull[len(hull) - 2], hull[len(hull) - 1], P[i]) < 0:
            hull.pop()
        hull.append(P[i])

    return hull, P


P = utils.dummy_simple_polygon()
shuffle(P)
hull, P = (GrahamScan(P, len(P)))
print("Hull:", hull)

import matplotlib.pyplot as plt

coord1 = P
coord1.append(coord1[0])
coord2 = hull
coord2.append(coord2[0])

xs1, ys1 = zip(*coord1)
xs2, ys2 = zip(*coord2)

plt.figure()
plt.plot(xs1, ys1)
plt.plot(xs2, ys2, marker='o', markersize=4, color="red")
plt.show()
