import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Calculadora Oxonia", page_icon="🧪", layout="centered")

# Regla: 70 ml por 30 L
ML_POR_30L = 70
L_BASE = 30

def oxonia_ml(litros_agua: float) -> float:
    """Regresa ml de Oxonia requeridos para X litros de agua."""
    return (litros_agua / L_BASE) * ML_POR_30L

def ml_a_litros(ml: float) -> float:
    return ml / 1000

# ---------------- UI ----------------
st.title("🧪 Calculadora de Oxonia")
st.caption("Regla: por cada 30 L de agua → 70 mL de Oxonia")
st.divider()

col1, col2 = st.columns(2)

with col1:
    tanque1 = st.number_input("Tanque 1 (L)", min_value=0.0, step=1.0, value=0.0)
with col2:
    tanque2 = st.number_input("Tanque 2 (L)", min_value=0.0, step=1.0, value=0.0)

proceso = st.number_input("Proceso (L)", min_value=0.0, step=1.0, value=0.0)

st.divider()

# Selección única: dónde se agrega el proceso
destino_proceso = st.radio(
    "¿A qué tanque se le suma el volumen del Proceso?",
    options=["No sumar proceso", "Sumar a Tanque 1", "Sumar a Tanque 2"],
    index=0,
    horizontal=True
)

# Aplicar lógica
tanque1_total = tanque1
tanque2_total = tanque2

if destino_proceso == "Sumar a Tanque 1":
    tanque1_total = tanque1 + proceso
elif destino_proceso == "Sumar a Tanque 2":
    tanque2_total = tanque2 + proceso

# Cálculos
ox1_ml = oxonia_ml(tanque1_total)
ox2_ml = oxonia_ml(tanque2_total)

ox1_l = ml_a_litros(ox1_ml)
ox2_l = ml_a_litros(ox2_ml)

st.subheader("✅ Resultados")

r1, r2 = st.columns(2)
with r1:
    st.metric("Tanque 1 - Agua considerada (L)", f"{tanque1_total:.1f}")
    st.metric("Tanque 1 - Oxonia (mL)", f"{ox1_ml:.1f}")
    st.metric("Tanque 1 - Oxonia (L)", f"{ox1_l:.3f}")

with r2:
    st.metric("Tanque 2 - Agua considerada (L)", f"{tanque2_total:.1f}")
    st.metric("Tanque 2 - Oxonia (mL)", f"{ox2_ml:.1f}")
    st.metric("Tanque 2 - Oxonia (L)", f"{ox2_l:.3f}")

st.divider()

total_agua = tanque1_total + tanque2_total
total_ox_ml = ox1_ml + ox2_ml
total_ox_l = ml_a_litros(total_ox_ml)

st.subheader("📌 Totales")
st.write(f"**Agua total considerada:** {total_agua:.1f} L")
st.write(f"**Oxonia total:** {total_ox_ml:.1f} mL  ({total_ox_l:.3f} L)")

st.info("Tip: Selecciona solo un destino para el Proceso (Tanque 1 o Tanque 2). Así evitamos sumar doble.")
