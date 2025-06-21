import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_tableau(tableau):
    return pd.DataFrame(tableau)

def plot_feasible_region(A, b):
    x = np.linspace(0, 10, 200)
    y1 = (b[0] - A[0][0] * x) / A[0][1]
    y2 = (b[1] - A[1][0] * x) / A[1][1]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=f'{A[0][0]}x + {A[0][1]}y ≤ {b[0]}', color='blue')
    plt.plot(x, y2, label=f'{A[1][0]}x + {A[1][1]}y ≤ {b[1]}', color='orange')
    plt.xlim((0, 10))
    plt.ylim((0, 20))
    plt.fill_between(x, np.minimum(y1, y2), where=(y1 >= 0) & (y2 >= 0), color='gray', alpha=0.3)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.grid(True)
    return plt
