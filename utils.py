import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_feasible_region(A, b, c):
    x = np.linspace(0, 20, 400)
    plt.figure(figsize=(8, 6))
    
    for i in range(A.shape[0]):
        if A[i, 1] != 0:
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            plt.plot(x, y, label=f"{A[i,0]}x + {A[i,1]}y <= {b[i]}")
    
    plt.xlim((0, 20))
    plt.ylim((0, 20))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Feasible Region")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt.gcf())

def display_tableau(tableau):
    st.write("### Simplex Tableau")
    st.dataframe(np.round(tableau, 3))
