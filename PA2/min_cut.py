import pprint
import random

from PA2.modules import graph, misc


def selectRandomEdge(G):
    degree = []
    index_vertex_map = {}
    v = list(G.keys())

    i = 0
    for k1 in v:
        degree.append(0)
        index_vertex_map[i] = k1
        for k2, v2 in G[k1].items():
            degree[i] += G[k1][k2]
        if i != 0:
            degree[i] += degree[i - 1]
        i += 1

    print("\nCumulative degree set 1:", degree)
    r = random.randint(1, degree[len(degree) - 1])
    print("Random Number:", r)
    index1 = misc.binarySearch(degree, 0, len(degree) - 1, r)
    vertex1 = index_vertex_map[index1]
    print("Index to Vertex Map:", index_vertex_map)
    print("Corresponding Vertex:", vertex1)

    degree = []
    neighbours = []
    index_vertex_map = {}

    for k, v in G[vertex1].items():
        if v != 0:
            neighbours.append(k)

    print("\nNeighbours of Vertex %s: %s" % (vertex1, neighbours))

    # cumulative degree

    i = 0
    for k, v in G[vertex1].items():
        sum = 0
        if k in neighbours:
            for k2, v2 in G[k].items():
                sum += v2
            degree.append(sum)
            index_vertex_map[i] = k
            if i != 0:
                degree[i] += degree[i - 1]
            i += 1

    print("Cumulative degree set 2:", degree)
    print("Index to Vertex Map:", index_vertex_map)
    r = random.randint(1, degree[len(degree) - 1])
    print("Random Number:", r)
    index2 = misc.binarySearch(degree, 0, len(degree) - 1, r)
    vertex2 = index_vertex_map[index2]
    print("Corresponding Vertex:", vertex2)

    vertex_lst = [vertex1, vertex2]
    vertex_lst.sort()

    print("\nUniformly selected edge: ", vertex_lst[0], vertex_lst[1])

    return vertex_lst[0], vertex_lst[1]


def contractEdge(G, vertex1, vertex2, map):
    print("\nVertex Map Before:", map)
    print()
    pprint.pprint(G)

    for k, v in G[vertex2].items():
        if k != vertex1:
            G[vertex1][k] += v

    G.pop(vertex2)

    for k1, v1 in G.items():
        for k2, v2 in G[k1].items():
            if k2 == vertex2 and k1 != vertex1:
                G[k1][vertex1] += v2

    for k1, v1 in G.items():
        G[k1].pop(vertex2)

    map[vertex1] += map[vertex2]
    map.pop(vertex2)
    print()
    print("Vertex Map After:", map)
    print()
    pprint.pprint(G)

    return G, map


def findMinCut(G):
    map = {}
    for i in range(1, len(G) + 1):
        map[i] = (i,)
    while len(G) != 2:
        v1, v2 = selectRandomEdge(G)
        G, map = contractEdge(G, v1, v2, map)

    lst = list(G.keys())
    min = G[lst[0]][lst[1]]

    print("\nMin Cut:", map[lst[0]], map[lst[1]])
    print("\nMin Cut value:", min)


G = graph.createRandomGraph()
findMinCut(G)
