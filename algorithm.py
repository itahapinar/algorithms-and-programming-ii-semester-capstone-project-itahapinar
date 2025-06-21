import numpy as np

def create_initial_tableau(A, b, c):
    m, n = A.shape
    T = np.zeros((m+1, n+m+1))
    T[:m, :n] = A
    T[:m, n:n+m] = np.eye(m)
    T[:m, -1] = b
    T[m, :n] = -c
    return T

def get_pivot_position(T):
    # 1) Entering variable (most negative in objective row)
    last = T[-1, :-1]
    if np.all(last >= 0):
        return None  # optimal
    j = np.argmin(last)

    # 2) Leaving variable (min positive ratio)
    col = T[:-1, j]
    rhs = T[:-1, -1]
    ratios = np.where(col > 0, rhs / col, np.inf)
    if np.all(ratios == np.inf):
        raise ValueError("Unbounded LP")
    i = np.argmin(ratios)
    return i, j

def pivot_step(T, i, j):
    T[i, :] /= T[i, j]
    for r in range(T.shape[0]):
        if r != i:
            T[r, :] -= T[r, j] * T[i, :]
    return T

def simplex_algorithm(A, b, c):
    T = create_initial_tableau(A, b, c)
    steps = [T.copy()]
    while True:
        p = get_pivot_position(T)
        if p is None:
            break
        i, j = p
        T = pivot_step(T, i, j)
        steps.append(T.copy())

    # Extract solution
    m, n = A.shape
    x = np.zeros(n)
    for var in range(n):
        col = T[:m, var]
        if np.count_nonzero(col) == 1 and (col == 1).any():
            row = np.where(col == 1)[0][0]
            x[var] = T[row, -1]
    z = T[-1, -1]
    return x, z, steps
