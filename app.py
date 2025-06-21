x, z, tableaus = simplex_algorithm(A, b, c)
st.success(f"Optimal x = {x.tolist()}, Max z = {z:.2f}")

for idx, T in enumerate(tableaus):
    st.markdown(f"### Step {idx}")
    st.dataframe(pd.DataFrame(T).style.format("{:.3f}"))
