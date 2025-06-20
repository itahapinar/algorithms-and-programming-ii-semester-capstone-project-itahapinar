import streamlit as st
import numpy as np
from algorithm import simplex

st.title("Simplex Yöntemi Çözücü")

st.subheader("Amaç Fonksiyonu (örnek: 3, 5):")
objective_input = st.text_input("z = ", "3, 5")

st.subheader("Kısıtlar (örnek: 1, 2, 8):")
num_constraints = st.number_input("Kaç adet kısıt girilecek?", min_value=1, step=1)
constraints = []

for i in range(num_constraints):
    constraint = st.text_input(f"{i+1}. Kısıt (örnek: 1, 2, 8)", "")
    constraints.append(constraint)

if st.button("Çözümle"):
    try:
        c = np.array([float(x) for x in objective_input.split(",")])

        A = []
        b = []

        for cons in constraints:
            parts = cons.split(",")
            A.append([float(x) for x in parts[:-1]])
            b.append(float(parts[-1]))

        A = np.array(A)
        b = np.array(b)

        solution, z_max, steps = simplex(c, A, b)

        st.success("Optimal Çözüm:")
        st.write("x =", solution)
        st.write("Maksimum Z =", z_max)

    except Exception as e:
        st.error(f"Hata: {e}")
