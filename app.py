import streamlit as st
import numpy as np
from algorithm import simplex
from utils import plot_feasible_region, display_tableau

st.set_page_config(page_title="Simplex Method Solver", layout="wide")
st.title("🔢 Linear Programming - Simplex Method (Interactive)")

st.markdown("""
This application solves **linear programming problems** using the **Simplex Method**.

- ✅ Enter the number of variables and constraints  
- ✅ Define objective function and constraints  
- ✅ Watch the algorithm step through the solution  
""")

# --- INPUT SECTION ---

st.sidebar.header("Step 1: Define Problem Dimensions")
num_vars = st.sidebar.number_input("Number of variables", min_value=2, max_value=5, value=2)
num_constraints = st.sidebar.number_input("Number of constraints", min_value=1, max_value=5, value=2)

st.header("Step 2: Enter Objective Function (Maximize)")
c = []
for i in range(num_vars):
    c.append(st.number_input(f"Coefficient of x{i+1} in Objective Function", key=f"c{i}", value=1.0))

st.header("Step 3: Enter Constraints (Ax ≤ b)")

A = []
b = []

for i in range(num_constraints):
    cols = st.columns(num_vars + 1)
    row = []
    for j in range(num_vars):
        row.append(cols[j].number_input(f"a{i+1}{j+1}", key=f"A{i}{j}", value=1.0))
    A.append(row)
    b.append(cols[-1].number_input(f"b{i+1}", key=f"b{i}", value=10.0))

A = np.array(A)
b = np.array(b)
c = np.array(c)

# --- SOLUTION SECTION ---
if st.button("🔍 Solve Linear Program"):
    try:
        solution, z_value, tableau = simplex(c, A, b)
        st.success(f"✅ Optimal solution found: x = {solution}, Max Value = {z_value:.2f}")
        display_tableau(tableau)

        if num_vars == 2:
            plot_feasible_region(A, b, c)
        else:
            st.warning("❗ Visualization only works for 2 variables.")

    except Exception as e:
        st.error(f"❌ Error: {e}")
