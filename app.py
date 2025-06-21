import streamlit as st
import numpy as np
from algorithm import simplex_method
from utils import plot_solution_space

st.title("Linear Programming - Simplex Method (Interactive)")

# Step 1: Problem setup
st.header("Step 1: Problem Setup")
num_vars = st.number_input("Number of variables", min_value=2, max_value=10, value=2, step=1)
num_constraints = st.number_input("Number of constraints", min_value=1, max_value=10, value=2, step=1)

# Step 2: Objective function
st.header("Step 2: Enter Objective Function (Maximize)")
st.subheader("Coefficients in Objective Function")

obj_coeffs = []
cols = st.columns(num_vars)
for i in range(num_vars):
    with cols[i]:
        coeff = st.number_input(f"Coefficient of x{i+1}", value=1.0, step=0.5, format="%.2f")
        obj_coeffs.append(coeff)

# Step 3: Constraints
st.header("Step 3: Enter Constraints (Ax ≤ b)")

constraint_matrix = []
constraint_rhs = []

for i in range(num_constraints):
    st.subheader(f"Constraint {i+1}")
    cols = st.columns(num_vars + 1)
    constraint_row = []
    
    for j in range(num_vars):
        with cols[j]:
            coeff = st.number_input(f"x{j+1} coefficient", key=f"const_{i}_{j}", value=1.0, step=0.5, format="%.2f")
            constraint_row.append(coeff)
    
    with cols[-1]:
        rhs = st.number_input("RHS (b)", key=f"rhs_{i}", value=10.0, step=0.5, format="%.2f")
    
    constraint_matrix.append(constraint_row)
    constraint_rhs.append(rhs)

# Solve button
if st.button("Solve Linear Program"):
    try:
        # Convert to numpy arrays
        c = np.array(obj_coeffs)
        A = np.array(constraint_matrix)
        b = np.array(constraint_rhs)
        
        # Solve using simplex method
        result = simplex_method(c, A, b)
        
        if result['status'] == 'optimal':
            st.success("Optimal solution found")
            st.write(f"Solution: x = {result['solution']}")
            st.write(f"Optimal Value: {result['value']:.2f}")
            
            # Visualization (for 2D problems)
            if num_vars == 2:
                fig = plot_solution_space(A, b, c, result['solution'])
                st.pyplot(fig)
            else:
                st.warning("Visualization only available for 2D problems")
                
            # Show simplex tableau if available
            if 'tableau' in result:
                st.subheader("Simplex Tableau")
                st.dataframe(result['tableau'])
                
        elif result['status'] == 'unbounded':
            st.error("Problem is unbounded")
        else:
            st.error("No feasible solution found")
            
    except Exception as e:
        st.error(f"Error solving problem: {str(e)}")