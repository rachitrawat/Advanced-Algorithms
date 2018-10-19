from PA2.modules import graph

G = graph.createRandomUDGraph()
v = len(G)
threshold = 2 * len(G) ** 3
print("\nThreshold:", threshold)

s = int(input("\nEnter s:"))
t = int(input("Enter t:"))
