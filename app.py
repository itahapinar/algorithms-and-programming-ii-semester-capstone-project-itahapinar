import streamlit as st
import numpy as np
from algorithm import simplex_method
from utils import plot_solution_space

st.title("Linear Programming - Simplex Method Visualizer")

# Örnek problem:
# Maximize: z = 3x + 2y
# Subject to:
#   x + y ≤ 4
#   2x + y ≤ 5
#   x, y ≥ 0

c = np.array([3, 2])
A = np.array([[1, 1], [2, 1]])
b = np.array([4, 5])

st.subheader("Feasible Region")
plot_solution_space(A, b)

st.subheader("Simplex Pivot Steps")
final_tableau, steps = simplex_method(c, A, b)

for i, step in enumerate(steps):
    st.write(f"### Step {i}")
    st.dataframe(step)

st.success(f"Optimal value: {final_tableau[-1, -1]}")
