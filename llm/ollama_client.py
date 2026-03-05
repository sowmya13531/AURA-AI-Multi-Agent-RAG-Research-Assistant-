import ollama

MODEL_NAME = "gemma:2b"

def generate_response(prompt: str) -> str:
    """
    Generate response from Ollama model.
    """

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Safe extraction
        if "message" in response and "content" in response["message"]:
            return response["message"]["content"]
        else:
            return "⚠️ Unexpected response format from Ollama."

    except Exception as e:
        return f"❌ Ollama Error: {str(e)}"