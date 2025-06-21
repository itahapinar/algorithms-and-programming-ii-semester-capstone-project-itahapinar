import numpy as np
import pandas as pd

def simplex_method(c, A, b, max_iter=1000):
    """
    Implement the simplex method for linear programming problems in standard form:
    Maximize c^T x subject to Ax <= b, x >= 0
    
    Returns a dictionary with:
    - 'status': 'optimal', 'unbounded', or 'infeasible'
    - 'solution': optimal solution if found
    - 'value': optimal value if found
    - 'tableau': final simplex tableau (optional)
    """
    # Convert to standard form
    m, n = A.shape
    c = np.array(c).reshape(-1)
    
    # Add slack variables
    tableau = np.zeros((m+1, n+m+1))
    tableau[:-1, :n] = A
    tableau[:-1, n:n+m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c
    
    # Basis keeps track of basic variables (slacks initially)
    basis = list(range(n, n+m))
    
    # Keep track of steps for tableau display
    tableaus = []
    
    for _ in range(max_iter):
        # Check for optimality
        if all(tableau[-1, :-1] >= -1e-8):
            # Prepare results
            solution = np.zeros(n + m)
            solution[basis] = tableau[:-1, -1]
            
            result = {
                'status': 'optimal',
                'solution': solution[:n],
                'value': tableau[-1, -1],
                'tableau': pd.DataFrame(tableau, 
                                      columns=[f"x{i+1}" for i in range(n)] + 
                                              [f"s{i+1}" for i in range(m)] + 
                                              ["RHS"])
            }
            return result
        
        # Select entering variable (most negative reduced cost)
        entering = np.argmin(tableau[-1, :-1])
        
        # Check for unboundedness
        if all(tableau[:-1, entering] <= 1e-8):
            return {'status': 'unbounded'}
        
        # Compute ratios for leaving variable
        ratios = tableau[:-1, -1] / tableau[:-1, entering]
        ratios[tableau[:-1, entering] <= 1e-8] = np.inf
        leaving = np.argmin(ratios)
        
        # Pivot
        pivot_val = tableau[leaving, entering]
        tableau[leaving, :] /= pivot_val
        
        for i in range(m+1):
            if i != leaving:
                tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]
        
        # Update basis
        basis[leaving] = entering
        
    return {'status': 'infeasible'}