import math
import random
import pprint


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


# no of vertices
v = random.randint(3, 6)

print("No of vertices: ", v)

G = {}
visited = []
degree = []

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

# cumulative degree
for i in range(1, v + 1):
    degree.append(0)
    for j in range(1, v + 1):
        degree[i - 1] += (G[i][j])
    if i != 1:
        degree[i - 1] += degree[i - 2]

print("\nCumulative degree set 1:", degree)

r = random.randint(1, degree[len(degree) - 1])
print("Random Number:", r)

index1 = binarySearch(degree, 0, len(degree) - 1, r)
vertex1 = index1 + 1

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
for k, v in G[index1].items():
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

print("\nUniformly selected edge: ", vertex1, vertex2)
