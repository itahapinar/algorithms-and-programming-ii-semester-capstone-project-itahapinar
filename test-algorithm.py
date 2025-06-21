import numpy as np
from algorithm import simplex

def test_simplex_solver():
    """
    Tests the simplex algorithm with a known problem and solution.
    This test corresponds to the example shown in the screenshots,
    where we are maximizing z = 3x1 + 2x2 to find the optimal point,
    even though the UI shows it as minimizing the negated objective.
    """
    # Objective function: Maximize z = 3x1 + 2x2
    # This is equivalent to minimizing -3x1 - 2x2
    c = np.array([3, 2])
    
    # Constraints:
    # 1x1 + 1x2 <= 4
    # 2x1 + 1x2 <= 5
    A = np.array([[1, 1], [2, 1]])
    b = np.array([4, 5])

    solution, max_value, _ = simplex(c, A, b)
    
    expected_solution = np.array([1., 3.])
    expected_max_value = 9.0

    assert np.allclose(solution, expected_solution, atol=1e-6), f"Test failed: Expected solution {expected_solution}, but got {solution}"
    assert np.isclose(max_value, expected_max_value, atol=1e-6), f"Test failed: Expected max value {expected_max_value}, but got {max_value}"
    
    print("Simplex algorithm test passed successfully!")

if __name__ == "__main__":
    test_simplex_solver()
