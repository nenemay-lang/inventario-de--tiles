
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Gestión de Insumos",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Sistema de Gestión de Stock de Insumos")

# INVENTARIO
df = pd.read_excel("Listado de insumos.xlsx")

df["STOCK MINIMO"] = pd.to_numeric(df["STOCK MINIMO"], errors="coerce")
df["EXISTENCIA"] = pd.to_numeric(df["EXISTENCIA"], errors="coerce")

df["STOCK MINIMO"] = df["STOCK MINIMO"].fillna(0)
df["EXISTENCIA"] = df["EXISTENCIA"].fillna(0)

# HISTORIAL
if os.path.exists("movimientos.csv"):
    movimientos = pd.read_csv("movimientos.csv")
else:
    movimientos = pd.DataFrame(
        columns=[
            "Fecha",
            "Tipo",
            "Producto",
            "Cantidad",
            "Persona",
            "Sector"
        ]
    )

# DASHBOARD
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

# INGRESOS
st.subheader("📥 Registrar Ingreso")

with st.form("ingreso"):

    prod_ing = st.selectbox(
        "Producto",
        df["PRODUCTO"]
    )

    cant_ing = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    guardar_ingreso = st.form_submit_button(
        "Registrar Ingreso"
    )

    if guardar_ingreso:

        nuevo = pd.DataFrame([{
            "Fecha": datetime.now(),
            "Tipo": "Ingreso",
            "Producto": prod_ing,
            "Cantidad": cant_ing,
            "Persona": "Depósito",
            "Sector": "Depósito"
        }])

        movimientos = pd.concat(
            [movimientos, nuevo],
            ignore_index=True
        )

        movimientos.to_csv(
            "movimientos.csv",
            index=False
        )

        st.success("Ingreso registrado")

st.divider()

# EGRESOS

st.subheader("📤 Registrar Retiro")

with st.form("egreso"):

    prod = st.selectbox(
        "Producto a entregar",
        df["PRODUCTO"]
    )

    cantidad = st.number_input(
        "Cantidad a retirar",
        min_value=1,
        step=1
    )

    persona = st.text_input(
        "Nombre de quien retira"
    )

    sector = st.text_input(
        "Sector"
    )

    guardar = st.form_submit_button(
        "Registrar Retiro"
    )

    if guardar:

        nuevo = pd.DataFrame([{
            "Fecha": datetime.now(),
            "Tipo": "Egreso",
            "Producto": prod,
            "Cantidad": cantidad,
            "Persona": persona,
            "Sector": sector
        }])

        movimientos = pd.concat(
            [movimientos, nuevo],
            ignore_index=True
        )

        movimientos.to_csv(
            "movimientos.csv",
            index=False
        )

        st.success("Retiro registrado")

st.divider()

# INVENTARIO

st.subheader("📦 Inventario")

st.dataframe(df)

# STOCK BAJO

st.subheader("⚠️ Productos con Stock Bajo")

stock_bajo = df[
    df["EXISTENCIA"]
    <= df["STOCK MINIMO"]
]

st.dataframe(stock_bajo)

# HISTORIAL

st.subheader("📑 Historial")

st.dataframe(
    movimientos.sort_index(
        ascending=False
    ),
    use_container_width=True
)
