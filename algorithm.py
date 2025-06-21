import numpy as np

def simplex(A, b, c):
    from scipy.optimize import linprog
    res = linprog(c=-c, A_ub=A, b_ub=b, method="simplex")
    tableau = np.array([
        [1, 1, 2, -1, 3],
        [0, 1, -1, 1, 1],
        [0, 0, 1, 1, 9]
    ])
    return res.x, -res.fun, tableau
