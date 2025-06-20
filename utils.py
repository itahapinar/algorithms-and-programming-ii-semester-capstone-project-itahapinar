import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

def plot_feasible_region(A, b, c):
    """
    Plot the feasible region for 2D linear programming problems
    """
    try:
        if A.shape[1] != 2:
            st.error("Plotting is only available for 2-variable problems")
            return
            
        fig, ax = plt.subplots(figsize=(10, 8))
        x = np.linspace(0, 25, 400)
        
        # Plot constraint lines
        colors = ['red', 'blue', 'green', 'orange', 'purple']
        
        for i in range(A.shape[0]):
            if abs(A[i, 1]) > 1e-10:  # Avoid division by zero
                y = (b[i] - A[i, 0] * x) / A[i, 1]
                # Only plot positive y values
                y = np.maximum(y, 0)
                color = colors[i % len(colors)]
                ax.plot(x, y, color=color, linewidth=2, 
                       label=f"{A[i,0]:.1f}x₁ + {A[i,1]:.1f}x₂ ≤ {b[i]:.1f}")
                
                # Fill the feasible region below the line
                ax.fill_between(x, 0, y, alpha=0.1, color=color)
            else:
                # Vertical line case
                if A[i, 0] != 0:
                    x_line = b[i] / A[i, 0]
                    if x_line >= 0:
                        ax.axvline(x=x_line, color=colors[i % len(colors)], 
                                 linewidth=2, label=f"{A[i,0]:.1f}x₁ ≤ {b[i]:.1f}")
        
        # Plot objective function direction
        if len(c) >= 2:
            # Draw some iso-profit lines
            max_val = max(np.max(b), 20)
            for val in [1, 5, 10]:
                if abs(c[1]) > 1e-10:
                    y_obj = (val - c[0] * x) / c[1]
                    ax.plot(x, y_obj, '--', alpha=0.5, color='black')
            
            # Add arrow showing objective direction
            ax.arrow(5, 5, c[0], c[1], head_width=0.5, head_length=0.5, 
                    fc='black', ec='black', alpha=0.7)
            ax.text(5 + c[0] + 1, 5 + c[1] + 1, 'Objective\nDirection', 
                   fontsize=10, ha='center')
        
        ax.set_xlim(0, 25)
        ax.set_ylim(0, 25)
        ax.set_xlabel('x₁', fontsize=12)
        ax.set_ylabel('x₂', fontsize=12)
        ax.set_title('Feasible Region and Constraints', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
    except Exception as e:
        st.error(f"Error plotting feasible region: {str(e)}")
        st.info("Make sure your problem has exactly 2 variables for visualization")

def display_tableau(tableau):
    """
    Display the simplex tableau in a formatted way
    """
    try:
        if tableau is None:
            st.warning("No tableau data available")
            return
            
        # Convert to numpy array if not already
        if not isinstance(tableau, np.ndarray):
            tableau = np.array(tableau)
            
        # Check if tableau has proper dimensions
        if tableau.size == 0:
            st.warning("Empty tableau")
            return
            
        st.write("### 📊 Final Simplex Tableau")
        
        # Create a more readable dataframe
        rows, cols = tableau.shape
        
        # Create column names
        n_vars = cols - rows  # Approximate number of original variables
        col_names = []
        
        # Original variables
        for i in range(max(2, n_vars)):
            col_names.append(f"x{i+1}")
            
        # Slack variables
        for i in range(rows - 1):
            col_names.append(f"s{i+1}")
            
        # RHS column
        col_names.append("RHS")
        
        # Adjust column names to match tableau size
        while len(col_names) < cols:
            col_names.append(f"Col{len(col_names)+1}")
        while len(col_names) > cols:
            col_names.pop()
            
        # Create row names
        row_names = []
        for i in range(rows - 1):
            row_names.append(f"Row {i+1}")
        row_names.append("Z")
        
        # Create DataFrame
        df = pd.DataFrame(
            np.round(tableau, 4), 
            columns=col_names[:cols],
            index=row_names
        )
        
        # Display with styling
        st.dataframe(
            df,
            use_container_width=True,
            height=min(400, (rows + 1) * 35)
        )
        
        # Add interpretation
        st.write("**Tableau Interpretation:**")
        st.write("- The last row shows the objective function coefficients")
        st.write("- The RHS column shows the current solution values")
        st.write("- Negative values in the last row indicate non-optimal solution")
        
    except Exception as e:
        st.error(f"Error displaying tableau: {str(e)}")
        st.write("Raw tableau data:")
        st.write(tableau)

def validate_problem(c, A, b):
    """
    Validate the linear programming problem inputs
    """
    errors = []
    warnings = []
    
    try:
        # Check dimensions
        if len(c) != A.shape[1]:
            errors.append("Number of objective coefficients must match number of variables")
            
        if len(b) != A.shape[0]:
            errors.append("Number of constraints must match constraint bounds")
            
        # Check for negative bounds
        if np.any(b < 0):
            errors.append("All constraint bounds must be non-negative")
            
        # Check for zero coefficients
        if np.all(c == 0):
            warnings.append("All objective coefficients are zero")
            
        # Check for infeasible constraints
        if np.any(np.all(A <= 0, axis=1) & (b > 0)):
            warnings.append("Some constraints may be infeasible")
            
        return errors, warnings
        
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return errors, warnings