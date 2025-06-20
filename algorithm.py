import numpy as np

def simplex(c, A, b):
    """
    Simplex method for solving linear programming problems (MAXIMIZATION)
    
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
    # [A | I | b]
    # [c | 0 | 0] <- objective row
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    
    # For maximization, we need to negate the objective coefficients
    # and add them to the bottom row
    cost_row = np.hstack([-c, np.zeros(m), [0]])
    tableau = np.vstack([tableau, cost_row])
    
    # Initialize basis (slack variables)
    basis = list(range(n, n + m))
    
    iteration = 0
    max_iterations = 1000
    
    while iteration < max_iterations:
        # Check optimality: all coefficients in objective row should be >= 0
        obj_row = tableau[-1, :-1]  # Exclude RHS
        min_coeff_idx = np.argmin(obj_row)
        
        if obj_row[min_coeff_idx] >= -1e-10:  # Optimal solution found
            break
        
        # Choose entering variable (most negative coefficient)
        pivot_col = min_coeff_idx
        
        # Find leaving variable using minimum ratio test
        pivot_col_values = tableau[:-1, pivot_col]  # Exclude objective row
        rhs_values = tableau[:-1, -1]  # RHS column, exclude objective row
        
        # Only consider positive pivot column values
        valid_ratios = []
        valid_rows = []
        
        for i in range(m):
            if pivot_col_values[i] > 1e-10:  # Positive pivot element
                ratio = rhs_values[i] / pivot_col_values[i]
                if ratio >= 0:  # Non-negative ratio
                    valid_ratios.append(ratio)
                    valid_rows.append(i)
        
        if not valid_ratios:
            raise Exception("Unbounded solution")
        
        # Choose minimum ratio
        min_ratio_idx = np.argmin(valid_ratios)
        pivot_row = valid_rows[min_ratio_idx]
        
        # Perform pivot operation
        pivot_element = tableau[pivot_row, pivot_col]
        
        # Make pivot element = 1
        tableau[pivot_row] = tableau[pivot_row] / pivot_element
        
        # Make all other elements in pivot column = 0
        for i in range(m + 1):  # Include objective row
            if i != pivot_row:
                multiplier = tableau[i, pivot_col]
                tableau[i] = tableau[i] - multiplier * tableau[pivot_row]
        
        # Update basis
        basis[pivot_row] = pivot_col
        iteration += 1
    
    if iteration >= max_iterations:
        raise Exception("Maximum iterations exceeded")
    
    # Extract solution
    solution = np.zeros(n)
    for i in range(m):
        var_index = basis[i]
        if var_index < n:  # Original variable (not slack)
            solution[var_index] = tableau[i, -1]
    
    # Calculate objective value
    z_value = tableau[-1, -1]  # This is already the correct maximization value
    
    return solution, z_value, tableau