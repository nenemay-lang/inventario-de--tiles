import pandas as pd
import sqlite3

df = pd.read_excel("Listado de insumos.xlsx")

conn = sqlite3.connect("insumos.db")

df.to_sql(
    "productos",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Base creada")
