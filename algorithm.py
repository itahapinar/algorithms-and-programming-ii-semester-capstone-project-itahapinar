import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost = np.hstack([c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost])

    basis = list(range(n, n + m))

    while True:
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            break

        ratios = []
        for i in range(m):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)

        pivot_row = np.argmin(ratios)
        if ratios[pivot_row] == np.inf:
            raise Exception("Unbounded solution")

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_element

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        basis[pivot_row] = pivot_col

    solution = np.zeros(n + m)
    for i in range(m):
        solution[basis[i]] = tableau[i, -1]

    return solution[:n], tableau
