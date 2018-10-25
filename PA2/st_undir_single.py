import random

from PA2.modules import graph


def check_connectivity(G, s, t):
    neighbours = []

    for k, v in G[s].items():
        if v != 0:
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


G = graph.createRandomGraph(False, True)
v = len(G)
threshold = 2 * v ** 3
print("\nThreshold:", threshold)

s = int(input("\nEnter s:"))
t = int(input("Enter t:"))
s_orig = s
bool = False
for i in range(1, threshold + 1):
    bool, vertex = check_connectivity(G, s, t)
    if not bool:
        s = vertex
    else:
        break

if bool:
    print("\nVertices %s and %s are in the same connected component!" % (s_orig, t))
else:
    print("\nVertices %s and %s are not in the same connected component!" % (s_orig, t))
