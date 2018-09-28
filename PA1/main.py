import pprint

G = {0: {1: 16, 2: 13},  # source
     1: {3: 12},
     2: {1: 4, 4: 14},
     3: {2: 9, 5: 20},
     4: {3: 7, 5: 4},
     5: {}  # sink
     }


def BFS(G, s, t):
    visited = []
    queue = []
    path = []
    prev_vertex = {}

    queue.append(s)
    visited.append(s)

    while queue:
        # dequeue
        v = queue.pop(0)
        print("\nDequeue: ", v)

        for vertex in list(G[v].keys()):
            if vertex not in visited and G[v][vertex] != 0:
                queue.append(vertex)
                visited.append(vertex)
                print("Enqueue: ", vertex)
                print("Mark: ", vertex)
                prev_vertex[vertex] = v

        print("Queue:", queue)
        print("Visited: ", visited)
        print()

        # shortest path
        if t in queue:
            path.append(5)
            while prev_vertex[t] != 0:
                path.append(prev_vertex[t])
                t = prev_vertex[t]
            path.append(0)
            path.reverse()
            break

    return path


# returns maximum flow from source s to sink t in graph G
def edmondsKarp(G, s, t):
    max_flow = 0
    print("\nResidual Graph: ")
    pprint.pprint(G)

    while True:
        path = BFS(G, s, t)
        if not path:
            break

        print("\n Shortest Path: ", path)

        min_capacity = 1000
        for idx, val in enumerate(path):
            if val != t and G[val][path[idx + 1]] <= min_capacity:
                min_capacity = G[val][path[idx + 1]]

        max_flow += min_capacity

        # augment the flow
        for idx, val in enumerate(path):
            if val != t:
                G[val][path[idx + 1]] -= min_capacity

        print("\nResidual Graph: ")
        pprint.pprint(G)

    print("Maximum Flow: ", max_flow)


edmondsKarp(G, 0, 5)
