import numpy as np

def simplex_method(c, A, b):
    """
    Solves the linear programming problem:
    Maximize: c^T * x
    Subject to: A * x <= b
    """

    num_constraints, num_variables = A.shape
    tableau = np.hstack((A, np.eye(num_constraints), b.reshape(-1, 1)))
    c_row = np.hstack((-c, np.zeros(num_constraints + 1)))
    tableau = np.vstack((tableau, c_row))

    steps = [tableau.copy()]  # Store each step

    while any(tableau[-1, :-1] < 0):
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = [
            tableau[i, -1] / tableau[i, pivot_col]
            if tableau[i, pivot_col] > 0 else np.inf
            for i in range(num_constraints)
        ]
        pivot_row = np.argmin(ratios)

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        steps.append(tableau.copy())

    return tableau, steps
