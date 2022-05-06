def FloydWarshall(n):
    inf = 99999
    # can change these values accordignly
    dists = [ [0, 5, inf, 2, inf],
              [inf, 0, 4, -2, 5],
              [inf, inf, 0, inf, inf],
              [1, 3, inf, 0, inf],
              [inf, inf, 4, 1, 0] ]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and (dists[i][k] + dists[k][j] < dists[i][j]):
                    dists[i][j] = dists[i][k] + dists[k][j]
        print("For k = ", k)
        print("")
        print_sol(n, dists)
        print(" ")


def print_sol(n, D):
    for i in range(n):
        for j in range(n):
            # ensures infinity is printed instead of an actual numerical value
            if D[i][j] > 999:
                print("inf", end = " ")
            else:
                print(D[i][j], end = " ")
        print(" ")
