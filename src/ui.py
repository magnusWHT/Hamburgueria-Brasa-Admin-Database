import streamlit as st

from src.db import consultar
from src.graficos import desenhar
from src.perguntas import NIVEIS, por_nível, resposta

def escrever(texto):
    st.markdown(texto.replace("$", "\\$"))

def mostrar_pergunta(p):
    with st.container(border=True):
        escrever(f"#### Q{p['numero']}. {p['titulo']}")
        escrever(p['enunciado'])
        st.caption("Conceitos: " + ", ".join(p['conceitos']))
        colunas = ", ".join(p['colunas_esperadas'])

        sql = resposta(p=p)

        if sql == "":
            st.info(f"Questão ainda não respondida. Colunas do resultado {colunas}")

            with st.expander("Dica"):
                escrever(p['dica'])
            return

        try:
            tabela = consultar(sql)
        except Exception as erro:
            st.error(f"Erro ao executar a consulta: {erro}")
            st.code(sql, language="sql")
            return

        if tabela.empty:
            st.warning("A consulta não retornou resultados. Verifique se a questão foi respondida corretamente.")
            return

        st.dataframe(tabela, hide_index=True, use_container_width=True)

        visual = p["visual"]
        campos_do_grafico = {
            "barra": ("x", "y"),
            "barra_agrupada": ("x", "y", "grupo"),
            "linha": ("x", "y"),
            "empilhada": ("x", "rotulo"),
            "barras_duplas": ("x", "y1", "y2"),
        }.get(visual["tipo"], ())
        colunas_do_grafico = {
            visual[campo]
            for campo in campos_do_grafico
            if campo in visual
        }
        colunas_do_grafico.update(visual.get("partes", []))
        ausentes = colunas_do_grafico.difference(tabela.columns)

        if visual["tipo"] == "tabela":
            return
        if ausentes:
            st.caption(
                "Resultado exibido em tabela. Gráfico indisponível: "
                "faltam as colunas " + ", ".join(sorted(ausentes)) + "."
            )
            return

        desenhar(tabela, visual, p["moeda"])


def mostrar_nível(nivel):
    titulo, descricao = NIVEIS[nivel]
    st.title(titulo)
    st.write(descricao)
    perguntas = por_nível(nivel)
    feitas = len([p for p in perguntas if resposta(p) != ""])

    st.progress(feitas / len(perguntas), text=f"{feitas} de {len(perguntas)} perguntas respondidas nesse nível.")
    for p in perguntas:
        mostrar_pergunta(p)