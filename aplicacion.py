import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.set_page_config(page_title="Stock Fotos", page_icon="📦")
st.title("📦 Contador de Productos")

if "productos" not in st.session_state:
    st.session_state.productos = {}

st.subheader("1) Carga tu base")
c1,c2,c3 = st.columns(3)
with c1: cod = st.text_input("Codigo")
with c2: nom = st.text_input("Nombre")
with c3: pre = st.number_input("Precio", min_value=0)
if st.button("Guardar"):
    if cod and nom and pre>0:
        st.session_state.productos[cod]={"nombre":nom,"precio":pre}
        st.success(f"Guardado {nom}")
st.write(st.session_state.productos)
st.divider()

st.subheader("2) Saca foto a TODOS los codigos juntos")
foto = st.camera_input("Tomar fotografia")
if foto:
    img = Image.open(foto)
    codigos = decode(img)
    if not codigos:
        st.error("No detecte nada, acerca mas")
    else:
        conteo={}
        for o in codigos:
            co=o.data.decode('utf-8')
            conteo[co]=conteo.get(co,0)+1
        total=0
        cant_total=0
        st.subheader("Resultado")
        for co,cant in conteo.items():
            p=st.session_state.productos.get(co)
            if p:
                sub=p["precio"]*cant
                total+=sub
                cant_total+=cant
                st.write(f"{cant} x {p['nombre']} = ${sub:,}")
            else:
                st.warning(f"{cant} x NO REGISTRADO: {co}")
        st.metric("TOTAL UNIDADES", cant_total)
        st.metric("TOTAL PLATA", f"${total:,}")
