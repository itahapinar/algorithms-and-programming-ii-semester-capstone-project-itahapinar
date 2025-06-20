from algorithm import simplex
import numpy as np

def test_simplex_basic():
    c = np.array([3, 2])
    A = np.array([[1, 1], [1, 0], [0, 1]])
    b = np.array([4, 2, 3])
    solution, value, _ = simplex(c, A, b)

    assert round(solution[0], 2) == 2.0
    assert round(solution[1], 2) == 2.0
    assert round(value, 2) == 10.0


