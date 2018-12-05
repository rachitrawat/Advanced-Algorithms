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
    P.remove(extreme_pt)

    dict_theta = {}
    dict_dist = {}
    dict = {}
    for i in range(1, len(P)):
        if extreme_pt[0] == P[i][0]:
            theta = 10 ** -100
        else:
            theta = (extreme_pt[1] - P[i][1]) / (extreme_pt[0] - P[i][0])
        dist = pow(extreme_pt[0] - P[i][0], 2) + pow(extreme_pt[1] - P[i][1], 2)

        dict_theta[tuple(P[i])] = theta
        dict_dist[tuple(P[i])] = dist
        dict[tuple(P[i])] = theta, dist

    sorted_lst = sorted(dict_theta.items(), key=operator.itemgetter(1))

    lst = []
    for idx, val in enumerate(sorted_lst):
        if idx == len(sorted_lst) - 1:
            lst.append(sorted_lst[idx][0])
        else:
            if sorted_lst[idx][1] == sorted_lst[idx + 1][1]:
                if dict_dist[sorted_lst[idx][0]] < dict_dist[sorted_lst[idx + 1][0]]:
                    lst.append(sorted_lst[idx + 1][0])
                    lst.append(sorted_lst[idx][0])
                else:
                    lst.append(sorted_lst[idx][0])
                    lst.append(sorted_lst[idx + 1][0])
            else:
                lst.append(sorted_lst[idx][0])

    print(lst)


P = utils.dummy_simple_polygon()
shuffle(P)
simple_polygon(P)
