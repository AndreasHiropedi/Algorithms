import sys
sys.setrecursionlimit(10000)

# Some coin systems:

lecture_coins = [1,5,7]    

sterling_coins = [1,2,5,10,20,50,100,200]


# Problem (1): Minimum number of coins (as in Lecture 17).

c_list = lecture_coins  # global variable, can set as desired

# Plain recursive implementation.
# fewest_coins should be implemented recursively, returning just smallest number of coins.

def fewest_coins(v):
    if v == 0:
        return 0
    total_coins = sys.maxsize
    for i in range(len(c_list)):
        if (c_list[i] <= v):
            subtotal = fewest_coins(v-c_list[i])
            if (subtotal != sys.maxsize and subtotal + 1 < total_coins):
                total_coins = subtotal + 1
    return total_coins

# slightly different method which returns a list of actual coins (which constitute a 
# minimum-sized solution).

def fewest_coins_list(v):
    if v == 0:
        return [0]*len(c_list)
    coins_used = []
    solutions = []
    for i in range(len(c_list)):
        if (c_list[i] <= v):
            coins_used = [c_list[i]] + fewest_coins_list(v - c_list[i])
            solutions.append(coins_used)
    for j in range(len(solutions)):
        new_group = []
        for element in solutions[j]:
            if element != 0:
                new_group.append(element)
        solutions[j] = new_group
    optimal = solutions[0]
    for elem in solutions:
        if len(elem) < len(optimal):
            optimal = elem
    return optimal


# Memoization operation, exactly as in our lecture:

def memoize(f):
    memo = {}
    def check(v):
        if v not in memo:
            memo[v] = f(v)
        return memo[v]
    return check

# memoize : (int->int) -> (int->int)
# f : int->int,  check : int->int

# To get the optimization of the recursion:

#fewest_coins = memoize(fewest_coins)
#fewest_coins_list = memoize(fewest_coins_list)

# NB. Can't change c_list after doing this!
# We would need to reload the file within the Python interpreter to use with new c_list.

# You should also implement and experiment with a dynamic programming solution,
# as given towards the end of slide-set 17.


def fewest_coins_dp(v):
    total = v
    k = len(c_list)
    S = [0] * k
    C = [float("inf")] * (v+1)
    P = [float("inf")] * (v+1)
    C[0] = 0
    for w in range(1, v+1):
        for i in range(0, k):
            if (c_list[i] <= w):
                if (C[w - c_list[i]] + 1 < C[w]):
                    C[w] = C[w - c_list[i]] + 1
                    P[w] = i
    while v > 0:
        i = P[v]
        S[i] = S[i] + 1
        v = v - c_list[i]
    return C[total]

def fewest_coins_list_dp(v):
    total = v
    k = len(c_list)
    S = [0] * k
    C = [float("inf")] * (v+1)
    P = [float("inf")] * (v+1)
    C[0] = 0
    for w in range(1, v+1):
        for i in range(0, k):
            if (c_list[i] <= w):
                if (C[w - c_list[i]] + 1 < C[w]):
                    C[w] = C[w - c_list[i]] + 1
                    P[w] = i
    while v > 0:
        i = P[v]
        S[i] = S[i] + 1
        v = v - c_list[i]
    coins_used = []
    for j in range(k):
        p = 0
        while p < S[j]:
            coins_used.append(c_list[j])
            p = p + 1
    return coins_used

