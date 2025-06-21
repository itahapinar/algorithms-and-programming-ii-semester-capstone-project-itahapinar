import streamlit as st
import numpy as np
from algorithm import simplex
from utils import display_tableau

st.title("Simplex Method Solver")

st.markdown("Enter your LP problem in standard form:")

c = st.text_input("Objective coefficients (e.g. 3,2):", "3,2")
A = st.text_area("Constraint coefficients (each row separated by newline):", "1,2\n4,0\n0,4")
b = st.text_input("Right-hand side values:", "8,16,12")

if st.button("Solve"):
    try:
        c = np.array([float(x) for x in c.split(",")])
        A = np.array([[float(num) for num in row.split(",")] for row in A.strip().split("\n")])
        b = np.array([float(x) for x in b.split(",")])

        final_tableau, basis, steps = simplex(c, A, b)

        for i, step in enumerate(steps):
            display_tableau(step, title=f"Step {i}")

        st.success(f"Optimal solution found. Z = {final_tableau[-1, -1]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
