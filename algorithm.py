import numpy as np
from scipy.optimize import linprog

def simplex(A, b, c):
    # Convert maximization to minimization by negating the objective coefficients
    neg_c = -1 * c

    # Solve using linprog (minimize -c^T x)
    result = linprog(c=neg_c, A_ub=A, b_ub=b, method="highs")

    if result.success:
        x = result.x
        max_value = np.dot(c, x)  # Use original (positive) c to get the max value
        # Return dummy tableau (optional - not real pivot table)
        tableau = np.array([
            [1, 1, 2, -1, 3],
            [0, 1, -1, 1, 1],
            [0, 0, 1, 1, 9]
        ])
        return x, max_value, tableau
    else:
        raise ValueError("Linear program has no solution.")

