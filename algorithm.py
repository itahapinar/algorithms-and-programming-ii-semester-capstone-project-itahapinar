import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost_row = np.hstack([-c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost_row])

    steps = []  # Pivot adımlarını tut
    while any(tableau[-1, :-1] < 0):
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios < 0] = np.inf
        pivot_row = np.argmin(ratios)
        pivot = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot

        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        steps.append(tableau.copy())

    solution = np.zeros(n)
    for i in range(n):
        col = tableau[:, i]
        if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
            row = list(col).index(1)
            solution[i] = tableau[row, -1]

    return solution, tableau[-1, -1], steps


