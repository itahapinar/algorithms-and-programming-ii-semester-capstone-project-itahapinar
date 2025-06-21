import numpy as np
from algorithm import simplex

def test_simple_case():
    c = np.array([3, 2])
    A = np.array([[1, 2], [4, 0], [0, 4]])
    b = np.array([8, 16, 12])
    solution, value, _ = simplex(c, A, b)
    assert np.allclose(solution, [4, 2])
    assert np.isclose(value, 18)

if __name__ == "__main__":
    test_simple_case()
    print("Test passed.")
