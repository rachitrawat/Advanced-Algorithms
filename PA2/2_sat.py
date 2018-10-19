import random

# n boolean variables
n = random.randint(3, 5)
# m clauses
m = random.randint(3, 5)
print("Number of variables:", n)
print("Number of clauses:", m)

exp = []

for i in range(1, m + 1):
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)

    if random.randint(0, 1) == 0:
        x = -1 * x

    if random.randint(0, 1) == 0:
        y = -1 * y

    exp.append([x, y])

print("\nExpression:", exp)

# initial assignment 1
assignment = [1] * n
print("Assignment:", assignment)

exp_eval = 1
for clause in exp:
    x = assignment[abs(clause[0])]
    y = assignment[abs(clause[1])]

    # if negation, invert truth value
    if clause[0] < 0:
        x = (x + 1) % 2
    if clause[1] < 0:
        y = (y + 1) % 2

    print("\nx%s: %s" % (clause[0], x))
    print("y%s: %s" % (clause[1], y))

    clause_eval = x + y
    print("Clause Eval:", clause_eval)
    exp_eval *= clause_eval
    print("Exp Eval:", exp_eval)
    print()
