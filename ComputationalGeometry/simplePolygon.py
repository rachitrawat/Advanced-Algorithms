"""
Python implementation of Simple Polygon,
"""

import operator
from random import shuffle

from ComputationalGeometry.modules import utils


def simple_polygon(P):
    final_pts = []

    max_x = max([item[0] for item in P])
    min_y = min([item[1] for item in P if item[0] == max_x])
    extreme_pt = [max_x, min_y]
    print("Extreme point:", extreme_pt)

    final_pts.append(extreme_pt)
    P.remove(extreme_pt)

    dict = {}
    dict_dist = {}
    for i in range(0, len(P)):
        if extreme_pt[0] == P[i][0]:
            final_pts.append(P[i])
        else:
            theta = (extreme_pt[1] - P[i][1]) / (extreme_pt[0] - P[i][0])
            dist = pow(extreme_pt[0] - P[i][0], 2) + pow(extreme_pt[1] - P[i][1], 2)

            dict_dist[tuple(P[i])] = dist

            if theta not in dict:
                dict[theta] = []

            if len(dict[theta]) > 0:
                lst = dict[theta]
                lst.append(P[i])
                for idx in range(0, len(dict[theta]) - 1):
                    if dist > dict_dist[tuple(dict[theta][idx])]:
                        lst.insert(idx, P[i])
                        lst.pop()
                dict[theta] = lst
            else:
                dict[theta].append(P[i])

    sorted_lst = sorted(dict.items(), key=operator.itemgetter(0))
    for element in sorted_lst:
        for point in element[1]:
            final_pts.append(point)

    return final_pts


P = utils.dummy_simple_polygon()
shuffle(P)
pts = simple_polygon(P)
print(pts)

import matplotlib.pyplot as plt

coord = pts
coord.append(coord[0])

xs, ys = zip(*coord)

plt.figure()
plt.plot(xs, ys)
plt.plot([pts[0][0]], [pts[0][1]], marker='o', markersize=4, color="red")
plt.show()
