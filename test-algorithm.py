import numpy as np
from algorithm import simplex

def test_simplex():
    c = np.array([3, 2])
    A = np.array([[1, 2], [4, 0], [0, 4]])
    b = np.array([8, 16, 12])
    result, basis, steps = simplex(c, A, b)
    assert round(result[-1, -1], 2) == 36.0

test_simplex()
