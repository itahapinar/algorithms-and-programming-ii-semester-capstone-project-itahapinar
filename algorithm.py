import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost = np.hstack([-c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost])

    basis = list(range(n, n + m))

    while True:
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            break

        valid_rows = [i for i in range(m) if tableau[i, pivot_col] > 0]
        if not valid_rows:
            raise Exception("Unbounded solution")

        ratios = [tableau[i, -1] / tableau[i, pivot_col] for i in valid_rows]
        pivot_row = valid_rows[np.argmin(ratios)]

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_element

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        basis[pivot_row] = pivot_col

    solution = np.zeros(n + m)
    for i in range(m):
        solution[basis[i]] = tableau[i, -1]

    z_value = -tableau[-1, -1]
    return solution[:n], z_value, tableau
