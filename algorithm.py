import numpy as np

class SimplexSolver:
    def __init__(self):
        self.max_iter = 1000  # Prevent infinite loops
    
    def solve(self, c, A, b):
        """
        Solve the linear programming problem:
        Maximize c^T x
        Subject to Ax <= b, x >= 0
        
        Returns a dictionary with:
        - 'status': 'optimal', 'unbounded', or 'infeasible'
        - 'x': optimal solution (if status is 'optimal')
        - 'value': optimal objective value
        - 'steps': list of simplex tableau steps
        """
        # Convert to standard form
        num_vars = len(c)
        num_constraints = len(b)
        
        # Add slack variables
        c_slack = np.zeros(num_constraints)
        c = np.concatenate([c, c_slack])
        
        A_slack = np.eye(num_constraints)
        A = np.hstack([A, A_slack])
        
        # Initial tableau
        tableau = self._create_initial_tableau(c, A, b)
        steps = [{'tableau': tableau.copy(), 'pivot_row': None, 'pivot_col': None}]
        
        # Simplex iterations
        for _ in range(self.max_iter):
            # Check if optimal
            if np.all(tableau[0, :-1] <= 0):
                break
                
            # Select entering variable (most positive coefficient)
            entering_col = np.argmax(tableau[0, :-1])
            
            # Compute ratios (only positive denominators)
            ratios = np.inf * np.ones(num_constraints)
            mask = tableau[1:, entering_col] > 0
            ratios[mask] = tableau[1:, -1][mask] / tableau[1:, entering_col][mask]
            
            # If all ratios are infinite, problem is unbounded
            if np.all(ratios == np.inf):
                return {'status': 'unbounded', 'steps': steps}
                
            # Select leaving variable (smallest positive ratio)
            leaving_row = np.argmin(ratios) + 1  # +1 because row 0 is objective
            
            # Pivot
            pivot_val = tableau[leaving_row, entering_col]
            tableau[leaving_row, :] /= pivot_val
            for i in range(tableau.shape[0]):
                if i != leaving_row:
                    tableau[i, :] -= tableau[i, entering_col] * tableau[leaving_row, :]
            
            # Record step
            steps.append({
                'tableau': tableau.copy(),
                'pivot_row': leaving_row,
                'pivot_col': entering_col
            })
        
        # Extract solution
        solution = np.zeros(num_vars + num_constraints)
        basis_indices = []
        
        # Find basic variables
        for col in range(num_vars + num_constraints):
            col_vec = tableau[:, col]
            if np.sum(col_vec == 1) == 1 and np.sum(col_vec != 0) == 1:
                row = np.where(col_vec == 1)[0][0]
                solution[col] = tableau[row, -1]
                if col < num_vars:  # Only count original variables
                    basis_indices.append(col)
        
        # Check for infeasibility
        if np.any(solution[num_vars:num_vars+num_constraints] < 0):
            return {'status': 'infeasible', 'steps': steps}
        
        return {
            'status': 'optimal',
            'x': solution[:num_vars],
            'value': -tableau[0, -1],  # Negate because we converted to standard form
            'c': c[:num_vars],
            'A': A[:, :num_vars],
            'b': b,
            'steps': steps
        }
    
    def _create_initial_tableau(self, c, A, b):
        """
        Create the initial simplex tableau in standard form.
        """
        num_vars = len(c)
        num_constraints = len(b)
        
        tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
        
        # Objective row
        tableau[0, :num_vars] = -c  # Negate because we're maximizing
        
        # Constraint rows
        tableau[1:, :num_vars] = A[:, :num_vars]
        tableau[1:, num_vars:num_vars+num_constraints] = np.eye(num_constraints)
        tableau[1:, -1] = b
        
        return tableau