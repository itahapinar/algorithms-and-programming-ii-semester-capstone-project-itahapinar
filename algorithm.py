import numpy as np

def simplex(c, A, b):
    """
    Simplex method for solving linear programming problems
    
    Parameters:
    c: objective function coefficients (to maximize)
    A: constraint matrix 
    b: constraint bounds
    
    Returns:
    solution: optimal solution vector
    z_value: optimal objective value
    tableau: final tableau
    """
    m, n = A.shape
    
    # Create initial tableau
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    cost = np.hstack([-c, np.zeros(m + 1)])
    tableau = np.vstack([tableau, cost])
    
    # Initialize basis (slack variables)
    basis = list(range(n, n + m))
    
    iteration = 0
    max_iterations = 1000  # Prevent infinite loops
    
    while iteration < max_iterations:
        # Check optimality condition
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= -1e-10:  # Use small epsilon for numerical stability
            break
        
        # Find pivot row using minimum ratio test
        valid_rows = [i for i in range(m) if tableau[i, pivot_col] > 1e-10]
        if not valid_rows:
            raise Exception("Unbounded solution")
        
        ratios = []
        for i in valid_rows:
            if tableau[i, pivot_col] > 1e-10:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(float('inf'))
        
        min_ratio_idx = np.argmin(ratios)
        pivot_row = valid_rows[min_ratio_idx]
        
        # Check for unbounded solution
        if ratios[min_ratio_idx] < 0:
            raise Exception("Infeasible solution")
        
        # Perform pivot operation
        pivot_element = tableau[pivot_row, pivot_col]
        if abs(pivot_element) < 1e-10:
            raise Exception("Degenerate pivot element")
            
        tableau[pivot_row] /= pivot_element
        
        # Update other rows
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]
        
        # Update basis
        basis[pivot_row] = pivot_col
        iteration += 1
    
    if iteration >= max_iterations:
        raise Exception("Maximum iterations exceeded")
    
    # Extract solution
    solution = np.zeros(n + m)
    for i in range(m):
        if basis[i] < len(solution):
            solution[basis[i]] = tableau[i, -1]
    
    # Calculate objective value
    z_value = -tableau[-1, -1]
    
    return solution[:n], z_value, tableau