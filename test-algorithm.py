import unittest
import numpy as np
from algorithm import simplex

class TestSimplex(unittest.TestCase):
    def test_basic_case(self):
        c = np.array([3, 2])
        A = np.array([[2, 1], [1, 2]])
        b = np.array([18, 14])
        solution, _, _ = simplex(c, A, b)  # 3 değişkeni de karşıla
        self.assertTrue(np.allclose(solution, [5.2, 4.4], atol=1e-1))

if __name__ == '__main__':
    unittest.main()
