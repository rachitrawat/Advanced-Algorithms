from PA4.modules import utils


def pointInsidePolygon(P, q):
    count = 0
    for idx, point in enumerate(P):
        if idx != len(P) - 1:
            if P[idx][0] <= q[0] <= P[idx + 1][0] or P[idx][0] >= q[0] >= P[idx + 1][0]:
                if P[idx][1] < q[1]:
                    count += 1
                    print(P[idx], P[idx + 1])

    if count % 2 == 1:
        return True
    else:
        return False


P = utils.dummy_simple_polygon()

q = [368, 308]

print("Point inside polygon: ", pointInsidePolygon(P, q))
