import unittest
import numpy as np
from algorithm import simplex

class TestSimplexMethod(unittest.TestCase):

    def test_basic_case(self):
        A = np.array([[1, 1], [2, 1]])
        b = np.array([4, 5])
        c = np.array([-3, -2])

        x, max_val, _ = simplex(A, b, c)

        # Check if the result is close to the known optimal solution
        self.assertAlmostEqual(x[0], 1, places=2)
        self.assertAlmostEqual(x[1], 3, places=2)
        self.assertAlmostEqual(max_val, 9.0, places=2)

if __name__ == '__main__':
    unittest.main()
