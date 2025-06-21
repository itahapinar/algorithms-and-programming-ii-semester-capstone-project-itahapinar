import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from algorithm import SimplexSolver
from utils import plot_solution_space

def main():
    st.title("Linear Programming - Simplex Method (Interactive)")
    st.write("This application solves linear programming problems using the Simplex Method.")

    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'show_steps' not in st.session_state:
        st.session_state.show_steps = False
    if 'solution' not in st.session_state:
        st.session_state.solution = None

    # Progress checklist
    with st.sidebar:
        st.subheader("Progress")
        step1_complete = st.checkbox("Enter the number of variables and constraints", 
                                    value=st.session_state.step > 1)
        step2_complete = st.checkbox("Define objective function and constraints", 
                                     value=st.session_state.step > 2)
        step3_complete = st.checkbox("Watch the algorithm step through the solution", 
                                     value=st.session_state.show_steps)

    # Step 1: Get problem dimensions
    if st.session_state.step == 1:
        st.subheader("Step 1: Enter Problem Dimensions")
        num_vars = st.number_input("Number of variables", min_value=1, value=2, step=1)
        num_constraints = st.number_input("Number of constraints", min_value=1, value=2, step=1)
        
        if st.button("Continue"):
            st.session_state.num_vars = num_vars
            st.session_state.num_constraints = num_constraints
            st.session_state.step = 2
            st.rerun()

    # Step 2: Get objective function and constraints
    elif st.session_state.step == 2:
        st.subheader("Step 2: Enter Objective Function (Maximize)")
        
        # Objective function coefficients
        st.write("### Enter coefficients for the objective function:")
        obj_coeffs = []
        for i in range(st.session_state.num_vars):
            coeff = st.number_input(f"Coefficient of x{i+1} in Objective Function", 
                                   value=3.0 if i == 0 else 2.0, step=0.5)
            obj_coeffs.append(coeff)
        
        st.subheader("Step 3: Enter Constraints (Ax ≤ b)")
        
        # Constraints matrix
        st.write("### Enter constraint coefficients:")
        constraint_matrix = []
        for i in range(st.session_state.num_constraints):
            st.write(f"#### Constraint {i+1}")
            row = []
            for j in range(st.session_state.num_vars):
                coeff = st.number_input(f"a{i+1}{j+1}", 
                                      value=1.0 if (i == 0 and j == 0) else 2.0 if (i == 1 and j == 0) else 1.0,
                                      key=f"a{i}{j}")
                row.append(coeff)
            b = st.number_input(f"b{i+1}", value=10.0, key=f"b{i}")
            row.append(b)
            constraint_matrix.append(row)
        
        if st.button("Solve Linear Program"):
            # Convert to numpy arrays
            c = np.array(obj_coeffs)
            A = np.array([row[:-1] for row in constraint_matrix])
            b = np.array([row[-1] for row in constraint_matrix])
            
            # Solve using simplex method
            solver = SimplexSolver()
            st.session_state.solution = solver.solve(c, A, b)
            st.session_state.step = 3
            st.rerun()

    # Step 3: Show solution
    elif st.session_state.step == 3:
        solution = st.session_state.solution
        st.subheader("Solution")
        
        if solution['status'] == 'optimal':
            st.success("Optimal solution found:")
            st.write(f"x = {solution['x']}")
            st.write(f"Max Value = {solution['value']:.2f}")
            
            # Plot solution space (for 2D problems)
            if st.session_state.num_vars == 2:
                fig = plot_solution_space(
                    solution['c'], 
                    solution['A'], 
                    solution['b'], 
                    solution['x']
                )
                st.pyplot(fig)
            
            # Show simplex tableau steps if requested
            st.session_state.show_steps = st.checkbox("Show step-by-step solution")
            
            if st.session_state.show_steps:
                st.subheader("Simplex Tableau Steps")
                for i, step in enumerate(solution['steps']):
                    with st.expander(f"Step {i+1}"):
                        st.write(f"**Pivot row:** {step['pivot_row']}, **Pivot column:** {step['pivot_col']}")
                        st.dataframe(pd.DataFrame(step['tableau']))
        
        elif solution['status'] == 'unbounded':
            st.error("Problem is unbounded - no optimal solution exists.")
        elif solution['status'] == 'infeasible':
            st.error("Problem is infeasible - no solution satisfies all constraints.")
        
        if st.button("Solve Another Problem"):
            st.session_state.step = 1
            st.session_state.show_steps = False
            st.session_state.solution = None
            st.rerun()

if __name__ == "__main__":
    main()