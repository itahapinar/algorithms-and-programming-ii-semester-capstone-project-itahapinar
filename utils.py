import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_solution_space(A, b, c, solution):
    """Plot the feasible region and solution for 2D LP problems"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot constraints
    x = np.linspace(0, max(b)*1.5, 400)
    
    for i in range(A.shape[0]):
        a1, a2 = A[i]
        rhs = b[i]
        
        if a2 != 0:
            y = (rhs - a1 * x) / a2
            mask = y >= 0
            ax.plot(x[mask], y[mask], label=f'{a1:.1f}x1 + {a2:.1f}x2 ≤ {rhs:.1f}')
            ax.fill_between(x[mask], 0, y[mask], alpha=0.1)
        else:
            # Vertical line
            x_val = rhs / a1
            ax.axvline(x=x_val, label=f'{a1:.1f}x1 ≤ {rhs:.1f}')
            ax.fill_betweenx([0, max(b)*1.5], 0, x_val, alpha=0.1)
    
    # Plot objective function
    if solution is not None:
        opt_x, opt_y = solution
        ax.plot(opt_x, opt_y, 'ro', markersize=10, label='Optimal Solution')
        
        # Objective function line
        y_obj = (c[0] * x) / -c[1]  # For visualization
        ax.plot(x, y_obj, '--', label=f'Objective: {c[0]:.1f}x1 + {c[1]:.1f}x2')
    
    ax.set_xlim(0, max(b)*1.2)
    ax.set_ylim(0, max(b)*1.2)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.legend()
    ax.grid(True)
    ax.set_title('Solution Space and Optimal Solution')
    
    return fig