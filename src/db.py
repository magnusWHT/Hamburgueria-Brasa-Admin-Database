import streamlit as st
import pandas as pd
import re

from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

SERVIDOR = r"D03S22-1252910\SQLEXPRESSSILVA"
BANCO = "HamburgueriaBrasa"
DRIVER = "ODBC Driver 18 for SQL Server"


def conectar():
    # Autenticação via Windows utilizando ODBC

    odbc = (
        f"DRIVER={{{DRIVER}}};SERVER={SERVIDOR};DATABASE={BANCO};"
        "Trusted_Connection=yes;TrustServerCertificate=yes"
    )

    return create_engine("mssql+pyodbc:///?odbc_connect="+quote_plus(odbc))

def consultar(sql):
    """Executa a consulta no sql server e devolve o resultado como tabela"""
    with conectar().connect() as conexao:
        return pd.read_sql_query(text(sql), conexao)

def mensagem_erro(erro):
    """Tira só a mensagem do SQL Server do meio do texto do erro."""
    achou = re.search(r"\[SQL Server\](.+?)\s*\(\d+\)", str(erro))
    return achou.group(1) if achou else str(erro)