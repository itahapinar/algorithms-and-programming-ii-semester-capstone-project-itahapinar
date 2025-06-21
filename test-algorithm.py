import unittest
import numpy as np
from algorithm import simplex

class TestSimplex(unittest.TestCase):
    def test_maximize(self):
        A = np.array([[1, 1], [2, 1]])
        b = np.array([4, 5])
        c = np.array([3, 2])
        x, max_val, _ = simplex(A, b, c)
        self.assertAlmostEqual(x[0], 1, places=2)
        self.assertAlmostEqual(x[1], 3, places=2)
        self.assertAlmostEqual(max_val, 9.0, places=2)

if __name__ == '__main__':
    unittest.main()
