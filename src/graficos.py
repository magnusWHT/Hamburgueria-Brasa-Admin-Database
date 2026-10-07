import streamlit as st

def texto_do_eixo(tabela, coluna, moeda):
    tabela = tabela.copy()

    if coluna in moeda:
        tabela[coluna] = tabela[coluna].map(lambda valor: f"R$ {valor:.2f}")
    elif coluna == "Mes":
        tabela[coluna] = tabela[coluna].map(lambda mes: f"{mes:02d}")
    else:
        tabela[coluna] = tabela[coluna].astype(str)
    return tabela

def numeros(tabela, moeda):
    """Mostra cada coluna da primeira linha como um número grande."""
    caixas = st.columns(len(tabela.columns))
    for caixa, coluna in zip(caixas, tabela.columns):
        valor = tabela[coluna].iloc[0]
        if coluna in moeda:
            valor = f"R$ {valor:.2f}"
        caixa.metric(coluna, str(valor))


def desenhar(tabela, visual, moeda):
    """Escolhe o gráfico certo para a pergunta."""
    tipo = visual["tipo"]
    if tabela.empty or tipo == "tabela":
        return
    if tipo == "metricas":
        numeros(tabela, moeda)
        return

    x = visual["x"]
    if tipo == "empilhada":  # junta número e nome do cliente: "#12 Ana"
        tabela = tabela.copy()
        tabela["Pedido"] = "#" + tabela[x].astype(str) + " " + tabela[visual["rotulo"]]
        x = "Pedido"
    tabela = texto_do_eixo(tabela, x, moeda)

    # sort=False mantém a ordem do ORDER BY da consulta.
    if tipo == "barra":
        deitado = visual.get("horizontal", False)
        st.bar_chart(tabela, x=x, y=visual["y"], horizontal=deitado, sort=False)
    elif tipo == "barra_agrupada":
        st.bar_chart(tabela, x=x, y=visual["y"], color=visual["grupo"], stack=False, sort=False)
    elif tipo == "linha":
        st.line_chart(tabela, x=x, y=visual["y"])
    elif tipo == "empilhada":
        st.bar_chart(tabela, x=x, y=visual["partes"], horizontal=True, sort=False)
    elif tipo == "barras_duplas":
        esquerda, direita = st.columns(2)
        esquerda.bar_chart(tabela, x=x, y=visual["y1"], horizontal=True, sort=False)
        direita.bar_chart(tabela, x=x, y=visual["y2"], horizontal=True, sort="-" + visual["y2"])
