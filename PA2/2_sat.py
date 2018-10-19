import random

# n boolean variables
n = random.randint(3, 5)
# m clauses
m = random.randint(3, 5)
print("Number of variables:", n)
print("Number of clauses:", m)

exp = []

for i in range(1, m):
    x = random.randint(1, n + 1)
    y = random.randint(1, n + 1)

    if random.randint(0, 1) == 0:
        x = -1 * x

    if random.randint(0, 1) == 0:
        y = -1 * y

    exp.append([x, y])

print("Expression:", exp)
