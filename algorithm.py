import numpy as np
from scipy.optimize import linprog

def simplex(A, b, c):
    # Note: Since linprog minimizes, we multiply c by -1 to maximize.
    res = linprog(c=-1 * c, A_ub=A, b_ub=b, method="highs")

    if res.success:
        # Reverse the sign to get the max value (because we minimized -c)
        max_value = np.dot(c, res.x)
        return res.x, max_value, res
    else:
        raise ValueError("Linear programming problem has no solution.")
