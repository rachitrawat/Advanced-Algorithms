import math
import pprint
import random


def createRandomGraph():
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
            if j not in G[i]:
                G[i][j] = 0

    m = 0
    for vertex1 in range(1, v + 1):
        for vertex2 in range(1, v + 1):
            if vertex2 != vertex1 and {vertex1, vertex2} not in visited:
                r = random.randint(0, 5)
                G[vertex1][vertex2] = r
                G[vertex2][vertex1] = r
                m += r
                visited.append({vertex1, vertex2})

    print("No of edges: ", m)
    print()
    pprint.pprint(G)
    return G


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
    index1 = binarySearch(degree, 0, len(degree) - 1, r)
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
    index2 = binarySearch(degree, 0, len(degree) - 1, r)
    vertex2 = index_vertex_map[index2]
    print("Corresponding Vertex:", vertex2)

    vertex_lst = [vertex1, vertex2]
    vertex_lst.sort()

    print("\nUniformly selected edge: ", vertex_lst[0], vertex_lst[1])

    return vertex_lst[0], vertex_lst[1]


def binarySearch(a, l, r, x):
    length = len(a)

    if r >= l:
        mid = math.ceil(l + (r - l) / 2)

        if a[mid] == x:
            return mid

        if x <= a[0]:
            return 0
        elif x >= a[length - 2]:
            return length - 1

        if a[mid] <= x <= a[mid + 1]:
            return mid + 1

        elif a[mid] > x:
            return binarySearch(a, l, mid - 1, x)
        else:
            return binarySearch(a, mid + 1, r, x)


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

    map[vertex1] += (vertex2,)
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

    print("\nMin Cut value:", min)


G = createRandomGraph()
findMinCut(G)
