import anthropic

client = anthropic.Anthropic(
api_key=tu clave aqui 
)

message = client.messages.create(
model="claude-3-5-sonnet-20240620",
max_tokens=1000,
messages=[
{"role": "user", "content": "Hola, ¿cómo estás?"}
]
print (message.content)


