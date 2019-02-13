"""
Implementation of s − t connectivity in a directed graph in Python.
"""

import math
import random

from RandomizedAlgorithms.modules import graph, misc


def check_connectivity(G, s, t, S):
    neighbours = []

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

    r = random.randint(0, len(neighbours) - 1)
    print("Random Number:", r)
    vertex = neighbours[r]
    print("Corresponding Vertex:", vertex)

    if vertex == t:
        return True, vertex
    else:
        return False, vertex


G = graph.createRandomGraph(True, True)
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
    print("\nVertices %s and %s are in the same connected component!" % (S, t))
else:
    print("\nVertices %s and %s are not in the same connected component!" % (S, t))
