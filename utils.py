import streamlit as st
import pandas as pd

def display_tableau(tableau, title="Tableau"):
    st.markdown(f"### {title}")
    df = pd.DataFrame(tableau)
    st.dataframe(df.style.format(precision=2))
