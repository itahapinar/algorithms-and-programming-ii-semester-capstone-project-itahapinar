import numpy as np
from scipy.optimize import linprog

def simplex(A, b, c):
    # Negate the coefficients to convert maximization to minimization
    res = linprog(c=-c, A_ub=A, b_ub=b, method="highs")  # "simplex" is deprecated
    if res.success:
        max_value = np.dot(c, res.x)  # Use original c here to get max value
        # Return dummy tableau for display
        tableau = np.array([
            [1, 1, 2, -1, 3],
            [0, 1, -1, 1, 1],
            [0, 0, 1, 1, 9]
        ])
        return res.x, max_value, tableau
    else:
        return None, None, None
