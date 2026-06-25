import streamlit as st
import base64
from anthropic import Anthropic

client = Anthropic("sk_ant_api03_fXY...UgAA")

st.title("Doctor de Plantas con IA")

uploaded_file = st.file_uploader("Sube una foto de la planta", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
st.image(uploaded_file, caption="Imagen cargada")
if st.button("Analizar"):
with st.spinner("Analizando..."):
image_data = base64.b64encode(uploaded_file.read()).decode('utf-8')
response = client.messages.create(
model="claude-3-5-sonnet-20240620",
max_tokens=1000,
messages=[
{"role": "user", "content": [
{"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}},
{"type": "text", "text": "Analiza esta planta, dime qué le ocurre y cómo tratarla."}
]}
]
)
st.write(response.content[0].text)

