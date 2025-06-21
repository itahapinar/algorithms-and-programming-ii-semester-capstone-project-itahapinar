import numpy as np
from algorithm import simplex_method

def test_simple_problem():
    c = np.array([3, 2])
    A = np.array([[1, 1], [2, 1]])
    b = np.array([4, 5])

    final_tableau, _ = simplex_method(c, A, b)
    optimal_value = final_tableau[-1, -1]

    assert round(optimal_value, 2) == 11.0

if __name__ == "__main__":
    test_simple_problem()
    print("Test passed.")
