import random

from PA2.modules import graph, misc


def check_connectivity(G, s, t):
    degree = []
    neighbours = []
    index_vertex_map = {}

    for k, v in G[s].items():
        if v != 0:
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
    r = random.randint(1, degree[len(degree) - 1])
    print("Random Number:", r)
    index2 = misc.binarySearch(degree, 0, len(degree) - 1, r)
    vertex2 = index_vertex_map[index2]
    print("Corresponding Vertex:", vertex2)

    if vertex2 == t:
        return True, vertex2
    else:
        return False, vertex2


G = graph.createRandomUDGraph()
v = len(G)
threshold = 2 * len(G) ** 3
print("\nThreshold:", threshold)

s = int(input("\nEnter s:"))
t = int(input("Enter t:"))

bool = False
for i in range(1, threshold + 1):
    bool, vertex = check_connectivity(G, s, t)
    if not bool:
        s = vertex
    else:
        break

if bool:
    print("\nVertices %s and %s are in the same connected component!" % (s, t))
else:
    print("\nVertices %s and %s are not in the same connected component!" % (s, t))
