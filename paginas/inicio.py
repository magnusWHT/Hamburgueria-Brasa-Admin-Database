import streamlit as st

from src.perguntas import NIVEIS, PERGUNTAS, resposta

st.image('https://img.freepik.com/vetores-premium/hamburguer-realista-no-fundo-do-quadro_91128-1527.jpg?w=2000', width=700)
st.title("Brasa & Pão - 1º trimestre de 2026")
st.write(
    "A Dona Marta precisa decidir quatro coisas antes de abril: **cardápio**, "
    "**entregador do trimestre**, **programa de fidelidade** e **bairros**. "
    "Neste painel, cada pergunta que você responder com SQL vira um gráfico."
)

feitas = len([p for p in PERGUNTAS if resposta(p) != ""])
st.progress(feitas / len(PERGUNTAS), text=f"**{feitas} de {len(PERGUNTAS)}** perguntas respondidas")

st.subheader("Como responder uma pergunta")
st.markdown(
    '''
1. Escreva a consulta e teste no **SSMS**.
2. Abra o arquivo **`src/respostas.py`** e encontre a pergunta (`Q1`, `Q2`...).
3. Cole a consulta entre as aspas triplas `"""`.
4. Dê às colunas os nomes pedidos em **Colunas do resultado**, usando `AS`.
5. Salve (**Ctrl+S**). O painel atualiza sozinho.
'''
)

st.subheader("Os três níveis")
for nivel, (titulo, descricao) in NIVEIS.items():
    st.page_link(f"paginas/nivel_{nivel}.py", label=f"{titulo}: {descricao}")

st.subheader("As tabelas do banco")
st.markdown(
    """
| Tabela | O que guarda | Ligação |
|---|---|---|
| **Clientes** | Quem compra: nome, bairro, telefone | - |
| **Entregadores** | Quem faz as entregas | - |
| **Produtos** | O cardápio (`Preco` = preço **atual**) | - |
| **Pedidos** | Cada pedido do trimestre | `IdCliente` → Clientes · `IdEntregador` → Entregadores (NULL na retirada) |
| **ItensPedido** | O que foi comprado em cada pedido (`PrecoUnitario` = preço **no dia**) | `IdPedido` → Pedidos · `IdProduto` → Produtos |
"""
)
st.caption("Regra de ouro: pedido cancelado não é venda. Faturamento = Quantidade × PrecoUnitario de ItensPedido.")