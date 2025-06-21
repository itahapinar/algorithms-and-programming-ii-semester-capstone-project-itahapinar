import streamlit as st
import pandas as pd

def display_tableau(tableau, title="Tableau"):
    df = pd.DataFrame(tableau)
    st.write(f"### {title}")
    st.dataframe(df.style.format(precision=2))
