import streamlit as st
from PIL import Image
import io
import os
from datetime import datetime

st.set_page_config(
    page_title="Contador de Productos",
    page_icon="📦",
    layout="centered"
)

st.title("📦 Contador de Productos")
st.write("Toma una foto de tus productos y registra la cantidad.")

if "total" not in st.session_state:
    st.session_state.total = 0

foto = st.camera_input("📷 Tomar fotografía")

if foto is not None:
    imagen = Image.open(foto)

    st.image(
        imagen,
        caption="Fotografía tomada",
        use_container_width=True
    )

    st.subheader("Cantidad de productos")

    cantidad = st.number_input(
        "Ingresa la cantidad que aparece en la fotografía:",
        min_value=0,
        step=1,
        value=0
    )

    if st.button("➕ Agregar al inventario"):
        st.session_state.total += cantidad
        st.success(
            f"Se agregaron {cantidad} productos correctamente."
        )

st.divider()

st.subheader("📊 Inventario")

st.metric(
    label="Total de productos",
    value=st.session_state.total
)

if st.button("🗑️ Reiniciar contador"):
    st.session_state.total = 0
    st.rerun()

st.divider()

st.caption(
    f"Última actualización: "
    f"{datetime.now().strftime('%d/%m/%Y %H:%M')}"
)
