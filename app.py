import streamlit as st
import numpy as np
from algorithm import simplex_method
from utils import plot_solution_space

st.title("📊 Simplex Method Visualizer")

st.markdown("## ➕ Objective Function")
num_vars = st.number_input("Number of variables", min_value=2, max_value=5, value=2)
c_input = st.text_input(f"Enter coefficients of the objective function (separated by commas)", "3, 2")

try:
    c = np.array([float(i.strip()) for i in c_input.split(",")])
    if len(c) != num_vars:
        st.error(f"Please enter exactly {num_vars} coefficients.")
        st.stop()
except:
    st.error("Invalid input for objective function coefficients.")
    st.stop()

st.markdown("## 📏 Constraints")
num_constraints = st.number_input("Number of constraints", min_value=1, max_value=5, value=2)

A = []
b = []

for i in range(num_constraints):
    col1, col2 = st.columns([3, 1])
    with col1:
        constraint_input = st.text_input(f"Constraint #{i+1} coefficients (e.g., 1, 2)", key=f"constraint_{i}")
    with col2:
        b_input = st.number_input(f"≤ b for constraint #{i+1}", key=f"b_{i}")
    
    try:
        coeffs = [float(x.strip()) for x in constraint_input.split(",")]
        if len(coeffs) != num_vars:
            st.error(f"Constraint #{i+1} must have {num_vars} coefficients.")
            st.stop()
        A.append(coeffs)
        b.append(b_input)
    except:
        st.error(f"Invalid input in constraint #{i+1}.")
        st.stop()

A = np.array(A)
b = np.array(b)

st.markdown("## ✅ Simplex Solution")

if st.button("Run Simplex Algorithm"):
    plot_solution_space(A, b) if num_vars == 2 else st.info("Visualization only available for 2 variables.")

    final_tableau, steps = simplex_method(c, A, b)

    for i, step in enumerate(steps):
        st.write(f"### Tableau - Step {i}")
        st.dataframe(np.round(step, 3))

    st.success(f"Optimal Value: {np.round(final_tableau[-1, -1], 3)}")
