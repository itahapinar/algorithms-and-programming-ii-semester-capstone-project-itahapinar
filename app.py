c = np.array([c1, c2])  # c1 = 3, c2 = 2 gibi

try:
    x, max_val, _ = simplex(A, b, c)
    st.success(f"✅ Optimal solution found: x = {x.tolist()}, Max Value = {max_val:.2f}")
except ValueError as e:
    st.error(str(e))
