import streamlit as st
import numpy as np
from algorithm import simplex
from utils import plot_feasible_region, display_tableau

st.set_page_config(page_title="Simplex Method Solver", layout="wide")

st.title("🔢 Linear Programming - Simplex Method")

st.markdown("""
This application solves linear programming problems using the **Simplex Method**.
Enter your coefficients below and visualize the solution process.
""")

with st.sidebar:
    st.header("Problem Parameters")
    c = st.text_input("Objective Function Coefficients (c)", "3,2")
    A = st.text_area("Constraint Coefficients (A)", "2,1\n1,2")
    b = st.text_input("Right-hand Side (b)", "18,14")

if st.button("Solve"):
    try:
        c = np.fromstring(c, sep=",")
        A = np.array([[float(num) for num in row.split(",")] for row in A.strip().split("\n")])
        b = np.fromstring(b, sep=",")

        solution, tableau = simplex(c, A, b)

        st.success(f"✅ Optimal solution found: x = {solution}, Max value = {np.dot(c, solution)}")
        display_tableau(tableau)
        plot_feasible_region(A, b, c)

    except Exception as e:
        st.error(f"❌ Error: {e}")
