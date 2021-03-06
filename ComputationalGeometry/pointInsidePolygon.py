"""
Python implementation of Point inside the polygon,
"""


from ComputationalGeometry.modules import utils


def pointInsidePolygon(P, q):
    count = 0
    for idx, point in enumerate(P):
        if idx != len(P) - 1:
            if P[idx][0] <= q[0] <= P[idx + 1][0] or P[idx][0] >= q[0] >= P[idx + 1][0]:
                if P[idx][1] < q[1]:
                    count += 1
                    print(P[idx], P[idx + 1])

    if count % 2 == 1:
        return True
    else:
        return False


P = utils.dummy_simple_polygon()

q = [368, 308]

print("Point inside polygon: ", pointInsidePolygon(P, q))

import matplotlib.pyplot as plt

coord = P
coord.append(coord[0])

xs, ys = zip(*coord)

plt.figure()
plt.plot(xs, ys)
plt.plot([q[0]], [q[1]], marker='o', markersize=4, color="red")
plt.show()
