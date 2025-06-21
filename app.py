import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from algorithm import simplex
from utils import display_tableau

st.set_page_config(page_title="Simplex Method App", layout="centered")

st.title("📊 Linear Programming: Simplex Method")
st.markdown("Follow the steps below to solve your LP problem using Simplex.")

# Step 2 - Objective function
st.header("Step 2: Enter Objective Function")
c_input = st.text_input("Enter objective function coefficients (e.g. 3,2):", "3,2")

# Step 3 - Constraints
st.header("Step 3: Enter Constraints")
A_input = st.text_area("Enter constraints (each row as comma-separated values):", "1,2\n4,0\n0,4")
b_input = st.text_input("Enter right-hand side values:", "8,16,12")

if st.button("Solve LP Problem"):
    try:
        c = np.array([float(x) for x in c_input.split(",")])
        A = np.array([[float(val) for val in row.split(",")] for row in A_input.strip().split("\n")])
        b = np.array([float(x) for x in b_input.split(",")])

        final_tableau, basis, steps = simplex(c, A, b)
        solution = np.zeros(len(c))
        for i, col in enumerate(basis):
            if col < len(c):
                solution[col] = final_tableau[i, -1]

        st.success("✅ Optimal solution found!")
        st.markdown(f"**Max Z = {final_tableau[-1, -1]:.2f}**")
        st.markdown("### Variable Values:")
        for i, val in enumerate(solution):
            st.write(f"x{i+1} = {val:.2f}")

        # Final Tableau
        display_tableau(final_tableau, "Final Tableau")

        # Visualization (Simple 2D feasible region + optimal point)
        if len(c) == 2:
            x_vals = np.linspace(0, max(b)*1.2, 400)
            fig, ax = plt.subplots()
            for i in range(A.shape[0]):
                if A[i,1] != 0:
                    ax.plot(x_vals, (b[i] - A[i,0]*x_vals) / A[i,1], label=f"Constraint {i+1}")
                else:
                    ax.axvline(x=b[i]/A[i,0], label=f"Constraint {i+1}")

            ax.plot(solution[0], solution[1], "ro", label="Optimal Point")
            ax.set_xlim(left=0)
            ax.set_ylim(bottom=0)
            ax.set_xlabel("x₁")
            ax.set_ylabel("x₂")
            ax.legend()
            ax.set_title("Feasible Region and Optimal Solution")
            st.pyplot(fig)
        else:
            st.info("Graphical visualization is only supported for 2-variable problems.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
