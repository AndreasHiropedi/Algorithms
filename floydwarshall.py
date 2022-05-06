def FloydWarshall(n):
    inf = 99999
    # can change these accordingly
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
    # printing out the final matrix
    for i in range(n):
        for j in range(n):
            # ensures infinity is printed
            if dists[i][j] > 999:
                print("inf", end = " ")
            else:
                print(dists[i][j], end = " ")
        print(" ")
