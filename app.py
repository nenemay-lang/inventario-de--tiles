
import streamlit as st

st.set_page_config(
    page_title="Gestión de Insumos",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Sistema de Gestión de Stock de Insumos")

st.markdown("""
### Bienvenida

Esta aplicación permitirá:

- Consultar stock.
- Registrar ingresos.
- Registrar egresos.
- Controlar stock mínimo.
- Generar alertas de reposición.
- Analizar consumo por sector.
""")

st.info("Versión 1 - Proyecto en desarrollo")
