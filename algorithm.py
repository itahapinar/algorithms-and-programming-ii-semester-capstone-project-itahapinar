import numpy as np

def create_initial_tableau(A, b, c):
    m, n = A.shape
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:-1, :n] = A
    tableau[:-1, n:n + m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c
    return tableau

def get_pivot_position(tableau):
    col = np.argmin(tableau[-1, :-1])
    if tableau[:-1, col].max() <= 0:
        return None  # Unbounded
    row_ratios = tableau[:-1, -1] / tableau[:-1, col]
    row_ratios[tableau[:-1, col] <= 0] = np.inf
    row = np.argmin(row_ratios)
    return row, col

def pivot_step(tableau, row, col):
    tableau[row] /= tableau[row, col]
    for r in range(len(tableau)):
        if r != row:
            tableau[r] -= tableau[r, col] * tableau[row]
    return tableau

def simplex_algorithm(A, b, c):
    tableaus = []
    tableau = create_initial_tableau(A, b, c)
    tableaus.append(tableau.copy())

    while True:
        pos = get_pivot_position(tableau)
        if pos is None:
            break  # Optimal or unbounded
        row, col = pos
        tableau = pivot_step(tableau, row, col)
        tableaus.append(tableau.copy())

        if (tableau[-1, :-1] >= 0).all():
            break  # Optimal reached

    solution = np.zeros_like(c)
    m, n = A.shape
    for i in range(n):
        col = tableau[:-1, i]
        if np.count_nonzero(col) == 1 and (col == 1).sum() == 1:
            one_index = np.where(col == 1)[0][0]
            solution[i] = tableau[one_index, -1]

    max_value = tableau[-1, -1]
    return solution, max_value, tableaus
