import numpy as np
from scipy.optimize import linprog
import numpy as np
from scipy.optimize import linprog

def simplex(A, b, c):
    # Negate c to convert maximization to minimization
    res = linprog(c=-c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    if res.success:
        x = res.x
        max_value = np.dot(c, x)  # NOT res.fun! Use original c here
        return x, max_value, res
    else:
        raise ValueError("No feasible solution.")
