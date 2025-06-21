import streamlit as st
import numpy as np
import pandas as pd
from algorithm import simplex
from utils import parse_input, tableau_to_dataframe

st.title("Simplex Method Solver")

with st.form("simplex_input"):
    c_str = st.text_area("Objective Function Coefficients (c)", "3 2")
    A_str = st.text_area("Constraint Coefficients (A)", "1 2\n4 0\n0 4")
    b_str = st.text_area("Right-hand side (b)", "8 16 12")
    submitted = st.form_submit_button("Solve")

if submitted:
    try:
        c, A, b = parse_input(c_str, A_str, b_str)
        c = np.array(c)
        A = np.array(A)
        b = np.array(b)

        solution, optimal_value, steps = simplex(c, A, b)

        st.success(f"Optimal Solution: {solution}")
        st.success(f"Optimal Value: {optimal_value}")

        st.subheader("Simplex Tableau Steps")
        for i, step in enumerate(steps):
            st.markdown(f"**Step {i}:**")
            df = tableau_to_dataframe(step)
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {str(e)}")
