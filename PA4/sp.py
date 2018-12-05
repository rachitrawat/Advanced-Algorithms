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
    print("\n", extreme_pt, end=',')
    P.remove(extreme_pt)

    dict = {}
    dict_dist = {}
    for i in range(0, len(P)):
        if extreme_pt[0] == P[i][0]:
            print(P[i], end=',')
        else:
            theta = (extreme_pt[1] - P[i][1]) / (extreme_pt[0] - P[i][0])
            dist = pow(extreme_pt[0] - P[i][0], 2) + pow(extreme_pt[1] - P[i][1], 2)

            dict_dist[tuple(P[i])] = dist

            if theta not in dict:
                dict[theta] = []

            if len(dict[theta]) > 0:
                lst = dict[theta]
                lst.append(P[i])
                for idx, pt in enumerate(dict[theta]):
                    if dist > dict_dist[tuple(pt)] and idx != len(dict[theta]) - 1:
                        lst.insert(idx, P[i])
                        lst.pop()
                dict[theta] = lst
            else:
                dict[theta].append(P[i])

    sorted_lst = sorted(dict.items(), key=operator.itemgetter(0))
    for element in sorted_lst:
        for point in element[1]:
            print(point, end=',')


P = utils.dummy_simple_polygon()
shuffle(P)
simple_polygon(P)
