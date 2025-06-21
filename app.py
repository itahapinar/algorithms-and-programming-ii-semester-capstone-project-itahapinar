
import streamlit as st
import numpy as np
from scipy.optimize import linprog

st.set_page_config(page_title="Linear Programming Solver", layout="centered")

st.markdown("## Step 2: Enter Objective Function (Maximize)")
c1 = st.text_input("Coefficient of x1 in Objective Function", "2.00")
c2 = st.text_input("Coefficient of x2 in Objective Function", "3.00")

st.markdown("## Step 3: Enter Constraints (Ax ≤ b)")
a11 = st.text_input("a11", "1.00")
a12 = st.text_input("a12", "1.00")
b1 = st.text_input("b1", "4.00")

a21 = st.text_input("a21", "2.00")
a22 = st.text_input("a22", "3.00")
b2 = st.text_input("b2", "9.00")

if st.button("🔷 Solve Linear Program"):
    try:
        # Nokta-virgül düzeltmesi ve float dönüşümü
        c = [-float(c1.replace(",", ".")), -float(c2.replace(",", "."))]
        A = [
            [float(a11.replace(",", ".")), float(a12.replace(",", "."))],
            [float(a21.replace(",", ".")), float(a22.replace(",", "."))]
        ]
        b = [float(b1.replace(",", ".")), float(b2.replace(",", "."))]

        result = linprog(c, A_ub=A, b_ub=b, method='highs')

        if result.success:
            x_vals = [round(v, 4) for v in result.x]
            max_val = round(-result.fun, 4)
            st.success(f"✅ Optimal solution found: x = {x_vals}, Max Value = {max_val}")
        else:
            st.error("❌ No feasible solution found.")
    except Exception as e:
        st.error(f"⚠️ Error in input or solving: {e}")