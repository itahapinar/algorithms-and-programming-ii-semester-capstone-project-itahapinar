import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost = np.hstack([-c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost])

    basis = list(range(n, n + m))
    steps = [tableau.copy()]

    while True:
        last_row = tableau[-1, :-1]
        if all(v >= 0 for v in last_row):
            break

        pivot_col = np.argmin(last_row)
        if all(tableau[:-1, pivot_col] <= 0):
            raise ValueError("Unbounded solution")

        ratios = [
            tableau[i, -1] / tableau[i, pivot_col]
            if tableau[i, pivot_col] > 0 else float('inf')
            for i in range(m)
        ]
        pivot_row = np.argmin(ratios)

        pivot = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot
        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        basis[pivot_row] = pivot_col
        steps.append(tableau.copy())

    return tableau, basis, steps
