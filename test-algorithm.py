import pytest
import numpy as np
from algorithm import SimplexSolver

def test_simplex_optimal():
    solver = SimplexSolver()
    c = np.array([3, 2])
    A = np.array([[1, 1], [2, 1]])
    b = np.array([10, 10])
    
    result = solver.solve(c, A, b)
    assert result['status'] == 'optimal'
    assert np.allclose(result['x'], [0, 10])
    assert np.isclose(result['value'], 20)

def test_simplex_unbounded():
    solver = SimplexSolver()
    c = np.array([1, 1])
    A = np.array([[-1, 1]])
    b = np.array([-1])
    
    result = solver.solve(c, A, b)
    assert result['status'] == 'unbounded'

def test_simplex_infeasible():
    solver = SimplexSolver()
    c = np.array([1, 1])
    A = np.array([[1, 1], [-1, -1]])
    b = np.array([-1, -2])
    
    result = solver.solve(c, A, b)
    assert result['status'] == 'infeasible']