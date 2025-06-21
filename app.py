if st.button("🔍 Solve Linear Program"):
    A = np.array([[a11, a12], [a21, a22]])
    b = np.array([b1, b2])
    c = np.array([c1, c2])  # örneğin: c1 = 3, c2 = 2

    try:
        x, max_val, res = simplex(A, b, c)
        st.success(f"✅ Optimal solution found: x = {x.tolist()}, Max Value = {max_val:.2f}")
    except ValueError as e:
        st.error(str(e))
