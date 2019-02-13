"""
Implementation of s − t connectivity in a directed multigraph in Python.
"""

import math
import random

from RandomizedAlgorithms.modules import graph, misc


def check_connectivity(G, s, t, S):
    degree = []
    neighbours = []
    index_vertex_map = {}
    no_neighbours = False

    if len(G[s]) == 0:
        no_neighbours = True

    # if no outgoing edge, return to S
    if no_neighbours:
        print("No Neighbours of %s" % s)
        return False, S
    else:
        for k, v in G[s].items():
            neighbours.append(k)

    print("\nNeighbours of Vertex %s: %s" % (s, neighbours))

    # cumulative degree

    i = 0
    for k, v in G[s].items():
        sum = 0
        if k in neighbours:
            for k2, v2 in G[k].items():
                sum += v2
            degree.append(sum)
            index_vertex_map[i] = k
            if i != 0:
                degree[i] += degree[i - 1]
            i += 1

    print("Cumulative degree set:", degree)
    print("Index to Vertex Map:", index_vertex_map)
    if len(degree) == 1:
        vertex2 = index_vertex_map[0]
        print("Corresponding Vertex:", vertex2)
    else:
        r = random.randint(1, degree[len(degree) - 1])
        print("Random Number:", r)
        index2 = misc.binarySearch(degree, 0, len(degree) - 1, r)
        vertex2 = index_vertex_map[index2]
        print("Corresponding Vertex:", vertex2)

    if vertex2 == t:
        return True, vertex2
    else:
        return False, vertex2


G = graph.createRandomGraph(True)
v = len(G)
threshold = v - 1
print("\nThreshold:", threshold)

s = int(input("\nEnter s:"))
t = int(input("Enter t:"))

bool = False
coin_break = True
S = s
while True:
    i = 0
    while i < threshold:
        coin_break = True
        bool, vertex = check_connectivity(G, s, t, S)
        if bool:
            break
        s = vertex
        i += 1

    if not bool:
        no_coins = math.ceil(math.log(v ** v, 2))
        print("\nFlipping coin %s times..." % no_coins)

        while no_coins != 0:
            if random.randint(0, 1) == 0:
                print("Tails")
                coin_break = False
                break
            else:
                print("Heads")
            no_coins -= 1

        if coin_break:
            break
        else:
            print("Continue loop...")
            continue
    break

if bool:
    print("\nVertices %s and %s are in the same connected component!" % (s, t))
else:
    print("\nVertices %s and %s are not in the same connected component!" % (s, t))
