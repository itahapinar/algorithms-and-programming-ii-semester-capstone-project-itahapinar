import streamlit as st
import numpy as np
from algorithm import simplex
from utils import plot_feasible_region

st.set_page_config(page_title="Simplex Solver", layout="centered")
st.title("🔺 Simplex Method Visualizer")

st.sidebar.header("Enter Problem Parameters")

c1 = st.sidebar.number_input("Objective: Coefficient of x", value=3.0)
c2 = st.sidebar.number_input("Objective: Coefficient of y", value=2.0)

A = np.array([
    [st.sidebar.number_input("a11", value=1.0), st.sidebar.number_input("a12", value=1.0)],
    [st.sidebar.number_input("a21", value=1.0), st.sidebar.number_input("a22", value=0.0)],
    [st.sidebar.number_input("a31", value=0.0), st.sidebar.number_input("a32", value=1.0)]
])
b = np.array([
    st.sidebar.number_input("b1", value=4.0),
    st.sidebar.number_input("b2", value=2.0),
    st.sidebar.number_input("b3", value=3.0)
])
c = np.array([c1, c2])

if st.button("Solve"):
    solution, max_val, steps = simplex(c, A, b)

    st.subheader("✅ Solution")
    st.write("Optimal solution (x, y):", solution)
    st.write("Maximum value of objective function:", max_val)

    st.subheader("📊 Graphical Representation")
    fig = plot_feasible_region(A, b, solution)
    st.pyplot(fig)

    st.subheader("📋 Pivot Steps")
    for i, tableau in enumerate(steps):
        st.markdown(f"**Step {i+1}**")
        st.dataframe(np.round(tableau, 2))


