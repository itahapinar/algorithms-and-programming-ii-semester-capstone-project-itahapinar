import matplotlib.pyplot as plt
import numpy as np

def plot_feasible_region(A, b, solution):
    x = np.linspace(0, 10, 400)
    plt.figure(figsize=(6, 6))
    
    for i in range(len(A)):
        y = (b[i] - A[i, 0]*x) / A[i, 1]
        plt.plot(x, y, label=f"{A[i,0]}x + {A[i,1]}y <= {b[i]}")

    plt.plot(solution[0], solution[1], 'ro', label='Optimal Point')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("Feasible Region")
    plt.legend()
    return plt
