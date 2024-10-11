import streamlit as st
import random

num = st.number_input("Digite um numero", step=1)

if num > 0:
    st.balloons()
    st.write("este numero é positivo")
elif num < 0:
    st.snow()
    st.write("este numero é negativo")
else:
    st.write("Este numero é nulo")