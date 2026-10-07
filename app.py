import streamlit as st

st.set_page_config(page_title="Brasa & Pão - Painel SQL", layout="wide")

st.navigation([
    st.Page("paginas/inicio.py", title="Início", default=True),
    st.Page("paginas/nivel_1.py", title="Nível 1 - Aquecimento"),
    st.Page("paginas/nivel_2.py", title="Nível 2 - Join"),
    st.Page("paginas/nivel_3.py", title="Nível 3 - Desafio")
]).run()
