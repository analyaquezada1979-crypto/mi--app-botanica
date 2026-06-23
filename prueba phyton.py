import streamlit as st
import anthropic

# Título de la app
st.title("🌱 App de Botánica Inteligente")

# Configura tu clave de API desde los 'Secrets' de Streamlit
api_key = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=api_key)

# Entrada de texto para el usuario
planta = st.text_input("¿Qué planta quieres consultar?")

if planta:
# Llamada a la IA
mensaje = f"Actúa como un experto en botánica. Dame información sobre los cuidados de la planta: {planta}"

response = client.messages.create(
model="claude-3-sonnet-20240229",
max_tokens=300,
messages=[{"role": "user", "content": mensaje}]
)

# Mostrar la respuesta
st.write(response.content[0].text)




