import ollama

modelfile = """FROM llama3.2

SYSTEM You are a very smart assistant who knows everything about the ocean.

PARAMETER temperature 0.1
"""

ollama.create(
    model="Knowitall",
    modelfile=modelfile
)

res = ollama.generate(
    model="Knowitall",
    prompt="Why is the ocean salty? Explain in 5 sentences."
)

print(res["response"])