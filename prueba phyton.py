


import streamlit as st
import anthropic

st.title("🌱 App de Botánica Inteligente")

api_key = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=api_key)

planta = st.text_input("¿Qué planta quieres consultar?")

if planta:
mensaje = f"Actúa como un experto en botánica. Dame información sobre los cuidados de la planta: {planta}"

response = client.messages.create(
model="claude-3-sonnet-20240229",
max_tokens=300,
messages=[{"role": "user", "content": mensaje}]
)

st.write(response.content[0].text)


