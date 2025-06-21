import numpy as np
import matplotlib.pyplot as plt

def plot_feasible_region(A, b):
    x = np.linspace(0, 10, 400)
    y1 = (b[0] - A[0][0] * x) / A[0][1]
    y2 = (b[1] - A[1][0] * x) / A[1][1]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='Constraint 1')
    plt.plot(x, y2, label='Constraint 2')
    plt.fill_between(x, 0, np.minimum(y1, y2), where=(y1 > 0) & (y2 > 0), alpha=0.3)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid(True)
    plt.legend()
    return plt
