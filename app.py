import streamlit as st
import numpy as np
from algorithm import simplex
from utils import display_tableau, plot_feasible_region

st.set_page_config(layout="wide", page_title="Simplex Solver", page_icon="📈")

st.title("Linear Programming - Simplex Method (Interactive)")

st.write("""
This application solves linear programming problems using the Simplex Method.
- **Step 1:** Define the size of your problem (number of variables and constraints).
- **Step 2:** Enter the coefficients of your objective function to be maximized.
- **Step 3:** Enter the coefficients of your constraints.
- **Step 4:** Click 'Solve' to see the optimal solution, the simplex tableau at each step, and a plot of the feasible region (for 2-variable problems).
""")

# Initialize session state
if 'solution' not in st.session_state:
    st.session_state.solution = None
    st.session_state.max_value = None
    st.session_state.steps = None
    st.session_state.c = None
    st.session_state.A = None
    st.session_state.b = None

# Step 1: Define problem size
st.header("Step 1: Define Problem Size")
col1, col2 = st.columns(2)
with col1:
    num_vars = st.number_input("Number of variables (x)", min_value=2, max_value=10, value=2, step=1)
with col2:
    num_constraints = st.number_input("Number of constraints", min_value=1, max_value=10, value=2, step=1)

# Step 2: Enter Objective Function
st.header("Step 2: Enter Objective Function (Maximize)")
c = np.zeros(num_vars)
cols = st.columns(num_vars)
for i in range(num_vars):
    with cols[i]:
        c[i] = st.number_input(f"Coefficient of x{i+1}", value=-3.0 if i == 0 else -2.0, key=f"c_{i}")

# Step 3: Enter Constraints
st.header("Step 3: Enter Constraints (Ax <= b)")
A = np.zeros((num_constraints, num_vars))
b = np.zeros(num_constraints)

# Create a grid for matrix A
for i in range(num_constraints):
    cols = st.columns(num_vars + 1)
    for j in range(num_vars):
        with cols[j]:
             default_a = 1.0
             if i == 1 and j == 0: default_a = 2.0
             A[i, j] = st.number_input(f"a{i+1},{j+1}", value=default_a, key=f"A_{i}_{j}")
    # Input for vector b in the last column
    with cols[num_vars]:
        default_b = 4.0 if i == 0 else 5.0
        b[i] = st.number_input(f"b{i+1}", value=default_b, key=f"b_{i}")

# Solve Button
if st.button("Solve Linear Program", key="solve_button"):
    with st.spinner("Solving..."):
        st.session_state.c = c
        st.session_state.A = A
        st.session_state.b = b
        
        solution, max_value, steps = simplex(c, A, b)
        
        st.session_state.solution = solution
        st.session_state.max_value = max_value
        st.session_state.steps = steps

# Display results if they exist in session state
if st.session_state.solution is not None:
    st.header("Results")
    if np.isinf(st.session_state.max_value):
        st.error("The problem is unbounded and has no optimal solution.")
    else:
        st.success(f"Optimal solution found: x = {np.round(st.session_state.solution, 2)}, Max Value = {st.session_state.max_value:.2f}")

    # Display Simplex Tableau Steps
    if st.session_state.steps:
        st.header("Simplex Tableau Steps")
        for i, step_tableau in enumerate(st.session_state.steps):
            display_tableau(step_tableau, i)

    # Plot Feasible Region
    if st.session_state.A.shape[1] == 2:
        plot_feasible_region(st.session_state.A, st.session_state.b, st.session_state.solution)
