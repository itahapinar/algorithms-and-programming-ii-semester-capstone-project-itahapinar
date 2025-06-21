import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from algorithm import simplex
from utils import plot_feasible_region, generate_tableau

st.set_page_config(page_title="Linear Programming - Simplex Method", layout="wide")

st.title("🔢 Linear Programming - Simplex Method (Interactive)")
st.markdown("""
This application solves **linear programming problems** using the Simplex Method.

✅ Enter the number of variables and constraints  
✅ Define objective function and constraints  
✅ Watch the algorithm step through the solution  
""")

st.subheader("Step 2: Enter Objective Function (Maximize)")
c1 = st.number_input("Coefficient of x1", value=-3.0, step=0.5)
c2 = st.number_input("Coefficient of x2", value=-2.0, step=0.5)

st.subheader("Step 3: Enter Constraints (Ax ≤ b)")
a11 = st.number_input("a11", value=1.0)
a12 = st.number_input("a12", value=1.0)
b1 = st.number_input("b1", value=4.0)

a21 = st.number_input("a21", value=2.0)
a22 = st.number_input("a22", value=1.0)
b2 = st.number_input("b2", value=5.0)

if st.button("🔍 Solve Linear Program"):
    A = np.array([[a11, a12], [a21, a22]])
    b = np.array([b1, b2])
    c = np.array([c1, c2])
    
    x, max_val, tableau = simplex(A, b, c)
    
    st.success(f"✅ Optimal solution found: x = {x.tolist()}, Max Value = {max_val:.2f}")
    
    st.subheader("Simplex Tableau")
    st.dataframe(generate_tableau(tableau))
    
    st.subheader("Feasible Region")
    fig = plot_feasible_region(A, b)
    st.pyplot(fig)
