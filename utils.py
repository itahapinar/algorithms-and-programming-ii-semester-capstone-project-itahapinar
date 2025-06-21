import pandas as pd

def parse_input(c_str, A_str, b_str):
    c = [float(i) for i in c_str.strip().split()]
    A = [[float(num) for num in row.strip().split()] for row in A_str.strip().split('\n')]
    b = [float(i) for i in b_str.strip().split()]
    return c, A, b

def tableau_to_dataframe(tableau):
    return pd.DataFrame(tableau)
