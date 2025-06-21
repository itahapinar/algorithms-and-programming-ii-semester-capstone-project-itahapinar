import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from algorithm import simplex_algorithm
from utils import plot_feasible_region

st.title("📊 Simplex Method with Tableau Visualization")

st.markdown("Define your LP problem:")

c1 = st.number_input("Coefficient of x1 in objective", value=3.0)
c2 = st.number_input("Coefficient of x2 in objective", value=2.0)

a11 = st.number_input("a11", value=1.0)
a12 = st.number_input("a12", value=1.0)
b1 = st.number_input("b1", value=4.0)

a21 = st.number_input("a21", value=2.0)
a22 = st.number_input("a22", value=1.0)
b2 = st.number_input("b2", value=5.0)

if st.button("Solve using Simplex"):
    A = np.array([[a11, a12], [a21, a22]])
    b = np.array([b1, b2])
    c = np.array([c1, c2])

    try:
        x, max_val, tableaus = simplex_algorithm(A, b, c)

        st.success(f"✅ Optimal x = {x.tolist()}, Max value = {max_val:.2f}")

        st.subheader("📋 Tableau Steps")
        for i, t in enumerate(tableaus):
            st.markdown(f"**Step {i}:**")
            df = pd.DataFrame(t)
            st.dataframe(df.style.format(precision=3))

        st.subheader("📈 Feasible Region")
        fig = plot_feasible_region(A, b)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
