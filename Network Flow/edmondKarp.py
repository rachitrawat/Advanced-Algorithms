"""
Implementation of the Edmonds-Karp algorithm in Python.
"""

import pprint

G = {0: {1: 16, 2: 13},  # 0 = source
     1: {3: 12},
     2: {1: 4, 4: 14},
     3: {2: 9, 5: 20},
     4: {3: 7, 5: 4},
     5: {}  # 5 = sink
     }


def bfs(G, s, t):
    visited = []
    queue = []
    path = []
    # for shortest path
    prev_vertex = {}

    # enqueue
    queue.append(s)
    visited.append(s)

    while queue:
        # dequeue
        v = queue.pop(0)
        print("\nDequeue: ", v)

        # get adjacent vertices to v
        for vertex in list(G[v].keys()):
            # enqueue only if
            # vertex is not visited
            # edge from v to vertex exists
            if vertex not in visited and G[v][vertex] != 0:
                queue.append(vertex)
                visited.append(vertex)
                print("Enqueue: ", vertex)
                print("Mark: ", vertex)
                # v is previous to vertex
                prev_vertex[vertex] = v

        print("Queue:", queue)
        print("Visited: ", visited)
        print()

        # shortest path
        if t in queue:
            path.append(t)
            while prev_vertex[t] != 0:
                path.append(prev_vertex[t])
                t = prev_vertex[t]
            path.append(0)
            path.reverse()
            break

    return path


# returns maximum flow from source s to sink t in graph G
def edmonds_karp(G, s, t):
    max_flow = 0

    print("\nResidual Graph: ")
    pprint.pprint(G)

    while True:
        path = bfs(G, s, t)
        # if no path exists from s to t
        if not path:
            break

        print("\nShortest Path: ", path)

        # base min_capacity = capacity of first edge in path
        min_capacity = G[0][path[1]]

        # find the minimum capacity
        for idx, val in enumerate(path):
            if val != t and G[val][path[idx + 1]] <= min_capacity:
                min_capacity = G[val][path[idx + 1]]

        print("Minimum Capacity: ", min_capacity)

        # flow augmentation by min_capacity
        for idx, val in enumerate(path):
            if val != t:
                # update forward flow in residual graph
                G[val][path[idx + 1]] -= min_capacity
                # update backward flow in residual graph
                if val not in G[path[idx + 1]]:
                    G[path[idx + 1]][val] = 0
                G[path[idx + 1]][val] += min_capacity

        # increase max_flow by min_capacity
        max_flow += min_capacity

        print("\nResidual Graph: ")
        pprint.pprint(G)

    print("Maximum Flow: ", max_flow)


edmonds_karp(G, 0, 5)
