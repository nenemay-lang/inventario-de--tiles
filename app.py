import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Gestión de Insumos",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Sistema de Gestión de Stock de Insumos")

# Cargar Excel
df = pd.read_excel("Listado de insumos.xlsx")

df["STOCK MINIMO"] = pd.to_numeric(df["STOCK MINIMO"], errors="coerce")
df["EXISTENCIA"] = pd.to_numeric(df["EXISTENCIA"], errors="coerce")

df["STOCK MINIMO"] = df["STOCK MINIMO"].fillna(0)
df["EXISTENCIA"] = df["EXISTENCIA"].fillna(0)

# Resumen
col1, col2, col3 = st.columns(3)

col1.metric("Total de Insumos", len(df))

col2.metric(
    "Stock Crítico",
    len(df[df["EXISTENCIA"] <= df["STOCK MINIMO"]])
)

col3.metric(
    "Existencia Total",
    df["EXISTENCIA"].sum()
)

st.divider()

st.subheader("Inventario")

st.dataframe(df, use_container_width=True)

st.subheader("Productos con Stock Bajo")

stock_bajo = df[df["EXISTENCIA"] <= df["STOCK MINIMO"]]

st.dataframe(stock_bajo, use_container_width=True)
