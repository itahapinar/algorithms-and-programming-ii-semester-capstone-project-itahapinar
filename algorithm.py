import numpy as np

def simplex(c, A, b):
    """
    Solves a linear programming problem in the form:
    Maximize z = c*x
    Subject to Ax <= b
               x >= 0

    Args:
        c (np.ndarray): Coefficients of the objective function.
        A (np.ndarray): Coefficients of the constraint inequalities.
        b (np.ndarray): Right-hand side values of the constraint inequalities.

    Returns:
        tuple: A tuple containing:
            - np.ndarray: The optimal solution for the variables.
            - float: The maximum value of the objective function.
            - list: A list of tableaus representing the steps of the simplex method.
    """
    m, n = A.shape

    # Create the initial tableau
    # [ A | I | b ]
    # [ -c| 0 | 0 ]
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost_row = np.hstack([-c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost_row])
    
    # Store history of tableaus for visualization
    tableaus = [tableau.copy()]

    # Iterate until all coefficients in the objective function row are non-negative
    while np.any(tableau[-1, :-1] < 0):
        # Find the pivot column (most negative value in the last row)
        pivot_col = np.argmin(tableau[-1, :-1])

        # Perform the minimum ratio test to find the pivot row
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        # Replace non-positive ratios with infinity to exclude them from min test
        ratios[ratios <= 0] = np.inf
        
        # If all ratios are infinity, the problem is unbounded
        if np.all(ratios == np.inf):
            return None, np.inf, tableaus

        pivot_row = np.argmin(ratios)
        
        # Normalize the pivot row
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_element

        # Eliminate other entries in the pivot column to make them zero
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]
        
        tableaus.append(tableau.copy())

    # Extract the solution from the final tableau
    solution = np.zeros(n)
    for i in range(n):
        col = tableau[:, i]
        # Check if the column is a basic variable column (contains a single 1 and rest are 0s)
        is_basic = np.count_nonzero(np.isclose(col, 1.0)) == 1 and \
                   np.count_nonzero(np.isclose(col, 0.0)) == len(col) - 1
        if is_basic:
            row_index = np.where(np.isclose(col, 1.0))[0][0]
            solution[i] = tableau[row_index, -1]
    
    # The maximum value of the objective function
    max_value = tableau[-1, -1]

    return solution, max_value, tableaus
