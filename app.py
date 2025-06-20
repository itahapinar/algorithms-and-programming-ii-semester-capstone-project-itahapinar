import streamlit as st
import numpy as np
from algorithm import simplex
from utils import plot_feasible_region, display_tableau

st.set_page_config(page_title="Simplex Method Solver", layout="wide")
st.title("🔢 Linear Programming - Simplex Method (Interactive)")

st.markdown("""
This application solves **linear programming problems** using the **Simplex Method**.

- ✅ Enter the number of variables and constraints  
- ✅ Define objective function and constraints  
- ✅ Watch the algorithm step through the solution  
""")

# --- INPUT SECTION ---

st.sidebar.header("Step 1: Define Problem Dimensions")
num_vars = st.sidebar.number_input("Number of variables", min_value=2, max_value=5, value=2)
num_constraints = st.sidebar.number_input("Number of constraints", min_value=1, max_value=5, value=2)

st.header("Step 2: Enter Objective Function (Maximize)")
c = []
for i in range(num_vars):
    c.append(st.number_input(f"Coefficient of x{i+1} in Objective Function", key=f"c{i}", value=1.0))

st.header("Step 3: Enter Constraints (Ax ≤ b)")

A = []
b = []

for i in range(num_constraints):
    cols = st.columns(num_vars + 1)
    row = []
    for j in range(num_vars):
        row.append(cols[j].number_input(f"a{i+1}{j+1}", key=f"A{i}{j}", value=1.0))
    A.append(row)
    b.append(cols[-1].number_input(f"b{i+1}", key=f"b{i}", value=10.0))

A = np.array(A, dtype=float)
b = np.array(b, dtype=float)
c = np.array(c, dtype=float)

# --- SOLUTION SECTION ---
if st.button("🔍 Solve Linear Program"):
    try:
        # Validate inputs
        if np.any(b < 0):
            st.error("❌ Error: All constraint bounds (b values) must be non-negative")
        elif A.size == 0 or c.size == 0:
            st.error("❌ Error: Invalid problem dimensions")
        else:
            # Solve the problem
            result = simplex(c, A, b)
            
            # Handle different return formats
            if len(result) == 3:
                solution, z_value, tableau = result
            elif len(result) == 2:
                solution, z_value = result
                tableau = None
            else:
                st.error("❌ Error: Unexpected return format from simplex function")
                st.stop()
            
            # Display results
            st.success(f"✅ Optimal solution found!")
            
            # Format solution display
            solution_text = ", ".join([f"x{i+1} = {solution[i]:.3f}" for i in range(len(solution))])
            st.write(f"**Optimal Solution:** {solution_text}")
            st.write(f"**Maximum Objective Value:** {z_value:.3f}")
            
            # Display tableau if available
            if tableau is not None:
                try:
                    display_tableau(tableau)
                except Exception as tableau_error:
                    st.warning(f"⚠️ Could not display tableau: {tableau_error}")
            
            # Plot feasible region for 2D problems
            if num_vars == 2:
                try:
                    plot_feasible_region(A, b, c)
                except Exception as plot_error:
                    st.warning(f"⚠️ Could not plot feasible region: {plot_error}")
            else:
                st.info("📊 Visualization is only available for 2-variable problems.")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("💡 Common issues:")
        st.info("- Check that all constraints are properly formatted")
        st.info("- Ensure the problem is feasible")
        st.info("- Verify that constraint bounds are non-negative")