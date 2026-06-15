import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": "In 3 bullet points, what are the most valuable AI skills a Filipino professional can learn in 2026?"}]
)
print(message.content[0].text)
