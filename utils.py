import matplotlib.pyplot as plt
import streamlit as st

def plot_solution_space(A, b):
    """
    Plots feasible region for 2-variable LP problems
    """
    import numpy as np

    x = np.linspace(0, 10, 400)
    plt.figure(figsize=(6, 6))

    for i in range(len(A)):
        if A[i][1] != 0:
            y = (b[i] - A[i][0] * x) / A[i][1]
            plt.plot(x, y, label=f'{A[i][0]}x + {A[i][1]}y ≤ {b[i]}')
    
    plt.xlim((0, 10))
    plt.ylim((0, 10))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Feasible Region')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
