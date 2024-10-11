import streamlit as st

"""
Test
A simple streamlit test.

"""

idade = st.number_input("Digite sua idade: ", min_value=14, max_value=120)
if idade>= 18:
    st.write(f"hello world - você é maior de idade: {idade}")
else:
    st.write(f"hello world - vai dormir")