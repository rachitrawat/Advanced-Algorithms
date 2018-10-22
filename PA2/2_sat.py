import random


def generate_random_exp():
    # n boolean variables
    n = random.randint(3, 5)
    # m clauses
    m = random.randint(3, 5)
    print("Number of variables:", n)
    print("Number of clauses:", m)

    exp = []

    for i in range(0, m):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)

        if random.randint(0, 1) == 0:
            x = -1 * x

        if random.randint(0, 1) == 0:
            y = -1 * y

        exp.append([x, y])

    print("Generated Expression:", exp)
    return n, exp


def evaluate_exp(exp, assignment):
    print("\nExpression:", exp)
    print("Assignment:", assignment)

    unsatisfied_clauses_idx = []
    unsatisfied_clauses = []
    exp_eval = 1
    for idx, clause in enumerate(exp):
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

        if clause_eval == 0:
            unsatisfied_clauses_idx.append(idx)
            unsatisfied_clauses.append(clause)

    if exp_eval != 0:
        print("Satisfying Assginment: ", assignment)
        return True, assignment

    # print("Unsatisfied clauses Index: ", unsatisfied_clauses_idx),
    print("Unsatisfied clauses: ", unsatisfied_clauses),
    return False, unsatisfied_clauses_idx


n, exp = generate_random_exp()
# initial assignment 1
assignment = [1] * n
bool, x = evaluate_exp(exp, assignment)

i = 2
while not bool:
    if i > 2 * pow(n, 2):
        print("Expression is not satisfiable!")
        break
    random_clause = x[random.randint(0, len(x) - 1)]
    print("Random Clause:", exp[random_clause])
    random_literal = exp[random_clause][random.randint(0, 1)]
    print("Random Literal:", random_literal)
    assignment[abs(random_literal)] = (assignment[abs(random_literal)] + 1) % 2
    bool, x = evaluate_exp(exp, assignment)
