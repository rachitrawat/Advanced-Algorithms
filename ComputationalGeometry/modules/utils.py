import operator


def dummy_simple_polygon():
    P = [[320, 368], [320, 384], [288, 384], [288, 380], [308, 380], [308, 376], [280, 376], [280, 392], [332, 392],
         [332, 364], [364, 364], [364, 352], [256, 352], [256, 404], [224, 404], [224, 332], [352, 332], [352, 288],
         [224, 288], [224, 312], [320, 312], [320, 300], [256, 300], [256, 296], [328, 296], [328, 320], [208, 320],
         [208, 280], [384, 280], [384, 340], [240, 340], [240, 396], [248, 396], [248, 348], [416, 348], [416, 272],
         [320, 272], [320, 256], [448, 256], [448, 320], [432, 320], [432, 340], [452, 340], [452, 224], [256, 224],
         [256, 244], [320, 244], [320, 248], [248, 248], [248, 216], [224, 216], [224, 240], [232, 240], [232, 256],
         [288, 256], [288, 264], [224, 264], [224, 272], [192, 272], [192, 416], [428, 416], [428, 384], [416, 384],
         [416, 400], [424, 400], [424, 408], [384, 408], [384, 384], [400, 384], [400, 396], [388, 396], [388, 404],
         [408, 404], [408, 372], [352, 372], [352, 404], [264, 404], [264, 368]]

    return P


def simple_polygon(P):
    final_pts = []

    max_x = max([item[0] for item in P])
    min_y = min([item[1] for item in P if item[0] == max_x])
    extreme_pt = [max_x, min_y]

    final_pts.append(extreme_pt)
    P.remove(extreme_pt)

    dict = {}
    dict_dist = {}
    for i in range(0, len(P)):
        if extreme_pt[0] == P[i][0]:
            final_pts.append(P[i])
        else:
            theta = (extreme_pt[1] - P[i][1]) / (extreme_pt[0] - P[i][0])
            dist = pow(extreme_pt[0] - P[i][0], 2) + pow(extreme_pt[1] - P[i][1], 2)

            dict_dist[tuple(P[i])] = dist

            if theta not in dict:
                dict[theta] = []

            if len(dict[theta]) > 0:
                lst = dict[theta]
                lst.append(P[i])
                for idx in range(0, len(dict[theta]) - 1):
                    if dist > dict_dist[tuple(dict[theta][idx])]:
                        lst.insert(idx, P[i])
                        lst.pop()
                dict[theta] = lst
            else:
                dict[theta].append(P[i])

    sorted_lst = sorted(dict.items(), key=operator.itemgetter(0))
    for element in sorted_lst:
        for point in element[1]:
            final_pts.append(point)

    return final_pts
