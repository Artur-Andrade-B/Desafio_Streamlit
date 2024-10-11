import streamlit as st
import random


st.title("Tente advinhar o numero, este foi gerado entre 0 e 100")

secretn = random.randint(0,100)

if 'secretn' not in st.session_state:
    st.session_state.secretn = secretn
    st.session_state.tentativas = 0

st.write(f"O numero esta entre {secretn-10} e {secretn+10}")
st.write(f"{st.session_state.secretn}")
guess = st.number_input("Digite o numero", step=1, 
                        min_value=0, max_value=100)

if st.button("tentar"):
    if guess == st.session_state.secretn:
        st.balloons()
        st.write(f"Voce acertou, o numero era {st.session_state.secretn}")
        st.session_state.clear()
        st.session_state.secretn = secretn
        st.session_state.tentativas = 0
        
    else:
        st.write(f"Voce errou, o numero era {st.session_state.secretn}")
        st.session_state.clear()

        