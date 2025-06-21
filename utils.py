import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def display_tableau(tableau, step_num):
    """
    Displays the simplex tableau as a pandas DataFrame.

    Args:
        tableau (np.ndarray): The simplex tableau.
        step_num (int): The current step number.
    """
    st.write(f"Simplex Tableau (Iteration {step_num})")
    num_vars = (tableau.shape[1] - 1) // 2 
    num_slack = num_vars
    
    columns = [f'x{i+1}' for i in range(num_vars)] + \
              [f's{i+1}' for i in range(num_slack)] + \
              ['b']
    
    df = pd.DataFrame(tableau, columns=columns)
    st.dataframe(df.style.format("{:.2f}"))


def plot_feasible_region(A, b, solution):
    """
    Plots the feasible region for a 2-variable linear programming problem.

    Args:
        A (np.ndarray): The constraint coefficients.
        b (np.ndarray): The constraint bounds.
        solution (np.ndarray): The optimal solution.
    """
    if A.shape[1] != 2:
        st.warning("Feasible region plot is only available for 2-variable problems.")
        return

    st.header("Feasible Region")

    fig = go.Figure()

    # Define a range for x and y axes
    d = np.linspace(-1, max(b)*2, 100)
    x, y = np.meshgrid(d,d)
    
    # Plot constraints
    for i in range(A.shape[0]):
        a1, a2 = A[i, 0], A[i, 1]
        b_val = b[i]
        
        y_vals = (b_val - a1 * d) / (a2 if a2 != 0 else 1e-9)

        fig.add_trace(go.Scatter(x=d, y=y_vals, mode='lines', name=f'{a1}x + {a2}y <= {b_val}'))

    # Add the feasible region by finding the area that satisfies all constraints
    # This is a simplified visualization and might not be perfect for all cases
    feasible_region = (A[0,0]*x + A[0,1]*y <= b[0])
    for i in range(1, A.shape[0]):
        feasible_region = np.logical_and(feasible_region, (A[i,0]*x + A[i,1]*y <= b[i]))
        
    # Non-negativity constraints
    feasible_region = np.logical_and(feasible_region, x >= 0)
    feasible_region = np.logical_and(feasible_region, y >= 0)
    
    # This contour plot is a trick to show the feasible area
    fig.add_trace(go.Contour(x=d, y=d, z=feasible_region.astype(int),
                             showscale=False,
                             colorscale=[[0, 'rgba(0,0,0,0)'], [1, 'rgba(0, 255, 0, 0.3)']]))

    # Plot the optimal solution point if it exists
    if solution is not None and len(solution) == 2:
        fig.add_trace(go.Scatter(x=[solution[0]], y=[solution[1]], mode='markers',
                                 marker=dict(color='red', size=12, symbol='star'),
                                 name='Optimal Solution'))

    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title="Feasible Region and Optimal Solution",
        xaxis=dict(range=[0,max(b)*1.5]),
        yaxis=dict(range=[0,max(b)*1.5])
    )
    fig.update_yaxes(scaleanchor = "x", scaleratio = 1)

    st.plotly_chart(fig)
