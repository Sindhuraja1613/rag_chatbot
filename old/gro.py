from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[{"role": "user", "content": "What is Groq?"}]
)