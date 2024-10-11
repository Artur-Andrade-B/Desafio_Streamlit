import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())

sum_preco = df["Preço"].sum()
lins = df.shape[0]

def verify_num(val):
    resp = val
    strug = str(int(val))
    lenger = len(strug)
    match lenger:
        case 3:
            resp = val
        case 4:
            resp = (strug[0] +"."+strug[1] +
                    strug[2]+" mil")
        case 5:
            resp = (strug[0] + strug[1] +
                    "." + strug[2]+" mil")
        case 6:
            resp = (strug[0] + strug[1] +
                    strug[2] + " mil")
        case 7:
            if strug[0] == "1":
                resp = (strug[0]+"."+strug[1] +
                        strug[2] + " milhão")
            else:
                resp = (strug[0]+"."+strug[1] +
                        strug[2] + " milhões")
    return resp

if st.button("todos"):
    st.balloons()
    st.metric('Receita',"R$ "+verify_num(sum_preco))
    st.metric('Quantidade de vendas (linhas)',verify_num(lins))
    st.metric('Quantidade de variáveis (colunas)',df.shape[1])
    st.dataframe(df)
else:
    st.write("clique no botão de todos")