import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def plot_solution_space(c, A, b, solution):
    """
    Plot the feasible region and optimal solution for a 2D LP problem.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot constraints
    x = np.linspace(0, max(10, solution[0]*1.5), 400)
    for i in range(len(b)):
        a1, a2 = A[i]
        if a2 != 0:
            y = (b[i] - a1 * x) / a2
            y[x > b[i]/a1 if a1 > 0 else x < b[i]/a1 if a1 < 0 else False] = np.nan
            ax.plot(x, y, label=f'{a1}x1 + {a2}x2 ≤ {b[i]}')
    
    # Find feasible region vertices
    vertices = []
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            a = A[[i, j]]
            b_vec = b[[i, j]]
            try:
                vertex = np.linalg.solve(a, b_vec)
                if np.all(A @ vertex <= b + 1e-8) and np.all(vertex >= -1e-8):
                    vertices.append(vertex)
            except np.linalg.LinAlgError:
                continue
    
    # Add axis intercepts
    for i in range(len(b)):
        if A[i, 0] != 0:
            vertex = np.array([b[i]/A[i, 0], 0])
            if np.all(A @ vertex <= b + 1e-8) and np.all(vertex >= -1e-8):
                vertices.append(vertex)
        if A[i, 1] != 0:
            vertex = np.array([0, b[i]/A[i, 1]])
            if np.all(A @ vertex <= b + 1e-8) and np.all(vertex >= -1e-8):
                vertices.append(vertex)
    
    # Plot feasible region
    if vertices:
        vertices = np.array(vertices)
        hull = vertices[vertices[:, 0].argsort()]
        feasible_poly = Polygon(hull, alpha=0.3, label='Feasible Region')
        ax.add_patch(feasible_poly)
    
    # Plot optimal solution
    ax.scatter(solution[0], solution[1], color='red', s=100, 
               label=f'Optimal Solution ({solution[0]:.2f}, {solution[1]:.2f})')
    
    # Plot objective function line
    if c[1] != 0:
        y_obj = ( -c[0] * x) / c[1]
        ax.plot(x, y_obj, '--', color='green', label='Objective Function')
    
    ax.set_xlim(0, max(10, solution[0]*1.2))
    ax.set_ylim(0, max(10, solution[1]*1.2))
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Solution Space')
    ax.grid(True)
    ax.legend()
    
    return fig