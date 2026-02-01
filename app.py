import streamlit as st
import json
import random
import math

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Calculadora Oxonia", page_icon="🧪", layout="centered")

# Regla: 70 mL por 30 L
ML_POR_30L = 70
L_BASE = 30

def oxonia_ml(litros_agua: float) -> float:
    """Regresa mL de Oxonia requeridos para X litros de agua."""
    return (litros_agua / L_BASE) * ML_POR_30L

def ceil_1_decimal(valor: float) -> float:
    """Redondea hacia arriba a 1 decimal."""
    return math.ceil(valor * 10) / 10

# ---------------- UI ----------------
st.title("🧪 Calculadora de Oxonia")
st.caption("Regla: por cada 30 L de agua → 70 mL de Oxonia")
st.divider()

col1, col2 = st.columns(2)

with col1:
    tanque1 = st.number_input("Tanque 1 (L)", min_value=0, step=1, value=0)
with col2:
    tanque2 = st.number_input("Tanque 2 (L)", min_value=0, step=1, value=0)

proceso = st.number_input("Proceso (L)", min_value=0, step=1, value=0)

st.divider()

# Selección única: dónde se agrega el proceso
destino_proceso = st.radio(
    "¿A qué tanque se le suma el volumen del Proceso?",
    options=["No sumar proceso", "Sumar a Tanque 1", "Sumar a Tanque 2"],
    index=0,
    horizontal=True
)

# Aplicar lógica (solo a un tanque)
tanque1_total = tanque1
tanque2_total = tanque2

if destino_proceso == "Sumar a Tanque 1":
    tanque1_total = tanque1 + proceso
elif destino_proceso == "Sumar a Tanque 2":
    tanque2_total = tanque2 + proceso

# ---------------- CÁLCULOS ----------------
# Calculamos en mL y redondeamos hacia arriba (evita subdosificación)
ox1_ml = math.ceil(oxonia_ml(tanque1_total))
ox2_ml = math.ceil(oxonia_ml(tanque2_total))

# Convertimos a litros y redondeamos hacia arriba a 1 decimal
ox1_l = ceil_1_decimal(ox1_ml / 1000)
ox2_l = ceil_1_decimal(ox2_ml / 1000)

# Totales (opcional pero útil)
total_ox_ml = ox1_ml + ox2_ml
total_ox_l = ceil_1_decimal(total_ox_ml / 1000)

# ---------------- RESULTADOS SIMPLES ----------------
st.subheader("🧪 Oxonia a agregar")

r1, r2 = st.columns(2)
with r1:
    st.metric("Tanque 1", f"{ox1_l} L")
with r2:
    st.metric("Tanque 2", f"{ox2_l} L")

st.divider()
st.metric("Oxonia total a preparar", f"{total_ox_l} L")

st.caption("Valores redondeados hacia arriba para asegurar concentración efectiva.")

