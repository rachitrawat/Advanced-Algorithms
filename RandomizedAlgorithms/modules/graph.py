import pprint
import random


def createRandomGraph(dir=False, single=False):
    while True:
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
                        r = 0
                        if single:
                            r = random.randint(0, 1)
                        else:
                            r = random.randint(0, 5)
                        if r == 0:
                            G[vertex1].pop(vertex2)
                            G[vertex2].pop(vertex1)
                        else:
                            G[vertex1][vertex2] = r
                            G[vertex2][vertex1] = r
                        m += r
                        visited.append({vertex1, vertex2})
                else:
                    r = 0
                    if vertex2 != vertex1:
                        if single:
                            r = random.randint(0, 1)
                        else:
                            r = random.randint(0, 5)
                        if r == 0:
                            G[vertex1].pop(vertex2)
                        else:
                            G[vertex1][vertex2] = r
                        m += r

        # remove disconnected vertices if undirected
        if not dir:
            for i in range(1, v + 1):
                if len(G[i]) == 0:
                    G.pop(i)

        # if G is empty
        if len(G) == 0:
            continue
        else:
            print("No of edges: ", m)
            print()
            pprint.pprint(G)
            return G
