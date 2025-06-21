import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from algorithm import simplex
from utils import parse_input, tableau_to_dataframe

st.title("Simplex Method Solver")

with st.form("simplex_input"):
    c_str = st.text_area("Objective Function Coefficients (c)", "3 2")
    A_str = st.text_area("Constraint Coefficients (A)", "1 2\n4 0\n0 4")
    b_str = st.text_area("Right-hand side (b)", "8 16 12")
    submitted = st.form_submit_button("Solve")

# Grafik çizimi fonksiyonu
def plot_feasible_region(A, b, c, optimal_solution):
    fig, ax = plt.subplots()
    x = np.linspace(0, 20, 400)

    colors = ['r', 'g', 'b', 'm', 'c', 'y']
    for i in range(len(A)):
        if A[i][1] != 0:
            y = (b[i] - A[i][0]*x) / A[i][1]
            ax.plot(x, y, label=f'{A[i][0]}x₁ + {A[i][1]}x₂ ≤ {b[i]}', color=colors[i % len(colors)])
        else:
            x_val = b[i] / A[i][0]
            ax.axvline(x=x_val, label=f'{A[i][0]}x₁ ≤ {b[i]}', color=colors[i % len(colors)])

    ax.set_xlim(0, max(10, optimal_solution[0] + 2))
    ax.set_ylim(0, max(10, optimal_solution[1] + 2))

    ax.plot(optimal_solution[0], optimal_solution[1], 'ko', label='Optimal Solution')
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.legend()
    ax.grid(True)
    ax.set_title("Feasible Region and Optimal Solution")
    return fig

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

        # Grafik çizimi (sadece 2 değişkenli durumlarda)
        if len(c) == 2:
            st.subheader("Feasible Region Plot")
            fig = plot_feasible_region(A, b, c, solution)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {str(e)}")
