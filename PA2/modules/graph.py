import pprint
import random


def createRandomGraph(dir=False):
    # no of vertices
    v = random.randint(3, 6)

    print("No of vertices: ", v)

    G = {}
    visited = []

    # create a dummy graph
    for i in range(1, v + 1):
        if i not in G:
            G[i] = {}
        for j in range(1, v + 1):
            if j not in G[i] and j != i:
                G[i][j] = 0

    m = 0
    for vertex1 in range(1, v + 1):
        for vertex2 in range(1, v + 1):
            if not dir:
                if vertex2 != vertex1 and {vertex1, vertex2} not in visited:
                    r = random.randint(1, 5)
                    G[vertex1][vertex2] = r
                    G[vertex2][vertex1] = r
                    m += r
                    visited.append({vertex1, vertex2})
            else:
                if vertex2 != vertex1:
                    r = random.randint(1, 5)
                    G[vertex1][vertex2] = r
                    m += r

    print("No of edges: ", m)
    print()
    pprint.pprint(G)
    return G
