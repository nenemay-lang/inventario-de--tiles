
# Sistema de Gestión de Stock de Insumos

## Objetivo

Desarrollar una aplicación web para la gestión y control de stock de insumos, permitiendo registrar ingresos y egresos, controlar existencias, generar alertas de reposición y obtener informes de consumo por sector.

---

## Funcionalidades

### Dashboard

- Total de insumos registrados.
- Total de movimientos.
- Insumos con stock crítico.
- Insumos con stock bajo.
- Últimos movimientos registrados.
- Consumo por sector.

---

### Gestión de Insumos

Campos:

- Código
- Producto
- Categoría
- Stock mínimo
- Stock actual
- Estado

Estados:

- OK
- Bajo stock
- Crítico
- Agotado

---

### Ingreso de Insumos

Registro de:

- Fecha
- Producto
- Cantidad ingresada
- Observaciones
- Usuario que registra

Acciones:

- Actualizar stock automáticamente.
- Registrar movimiento en historial.

---

### Entrega de Insumos

Registro de:

- Fecha
- Producto
- Cantidad entregada
- Persona que retira
- Sector
- Unidad Funcional
- Observaciones

Acciones:

- Descontar stock automáticamente.
- Registrar movimiento en historial.

---

### Alertas Automáticas

Generar alertas cuando:

- El stock sea menor al stock mínimo.
- El stock llegue a cero.

Indicadores:

🟢 Normal

🟡 Bajo stock

🔴 Crítico

⚫ Agotado

---

### Compras

Generación automática de listado de reposición.

Información:

- Código
- Producto
- Stock actual
- Stock mínimo
- Cantidad sugerida de compra

Exportable a Excel.

---

### Reportes

#### Consumo por sector

- Convenios
- Inversiones
- Operaciones
- Comercio Exterior
- Contabilidad
- Atención al Cliente
- Otros

#### Consumo por usuario

Cantidad de insumos retirados por persona.

#### Consumo por producto

Ranking de artículos más utilizados.

#### Historial de movimientos

Registro completo de ingresos y egresos.

---

## Estructura de Datos

### Productos

| Campo |
|---------|
| Código |
| Producto |
| Categoría |
| Stock Mínimo |
| Stock Actual |
| Estado |

### Movimientos

| Campo |
|---------|
| Fecha |
| Tipo Movimiento |
| Código |
| Producto |
| Cantidad |
| Usuario |
| Sector |
| Unidad Funcional |
| Observaciones |

### Sectores

| Campo |
|---------|
| Nombre Sector |
| Unidad Funcional |

---

## Tecnología

### Backend

Python

### Frontend

Streamlit

### Base de Datos

SQLite

### Repositorio

GitHub

---

## Fases del Proyecto

### Versión 1

- Gestión de stock.
- Registro de ingresos.
- Registro de egresos.
- Alertas de stock mínimo.

### Versión 2

- Reportes.
- Dashboard.
- Exportación a Excel.

### Versión 3

- Gestión de usuarios.
- Roles y permisos.
- Notificaciones automáticas.

---

## Fuente de Datos Inicial

- Listado de insumos.xlsx
- INVENTARIO 2025 - 05 - 22 (version 1).xlsx

---

## Responsable Funcional

Irene Silvia May
