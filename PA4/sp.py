import operator
from operator import itemgetter
from random import shuffle

from PA4.modules import utils


def simple_polygon(P):
    P = sorted(P, key=itemgetter(0), reverse=True)
    extreme_pt = [P[0][0]]

    lst = []
    for pt in P:
        if P[0][0] == pt[0]:
            lst.append(pt[1])
        else:
            extreme_pt.append(min(lst))
            break

    print("Extreme point:", extreme_pt)

    dict_theta = {}
    dict_dist = {}
    for i in range(1, len(P)):
        if extreme_pt[0] == P[i][0]:
            theta = 10 ** -100
        else:
            theta = (extreme_pt[1] - P[i][1]) / (extreme_pt[0] - P[i][0])
        dist = pow(extreme_pt[0] - P[i][0], 2) + pow(extreme_pt[1] - P[i][1], 2)

        dict_theta[tuple(P[i])] = theta
        dict_dist[tuple(P[i])] = dist

    sorted_lst = sorted(dict_theta.items(), key=operator.itemgetter(1))
    print(sorted_lst)


P = utils.dummy_simple_polygon()
shuffle(P)
simple_polygon(P)
