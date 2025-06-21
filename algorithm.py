import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    tableau = np.zeros((m + 1, n + m + 1))
    
    tableau[:-1, :n] = A
    tableau[:-1, n:n + m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c

    basis = list(range(n, n + m))
    
    steps = [tableau.copy()]  # her adımı kaydet
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
            raise ValueError("Problem is unbounded.")

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        basis[pivot_row] = pivot_col
        steps.append(tableau.copy())

    solution = np.zeros(n + m)
    for i in range(m):
        solution[basis[i]] = tableau[i, -1]

    return solution[:n], tableau[-1, -1], steps
