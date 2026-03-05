from llm.ollama_client import generate_response


def plan_research(question: str) -> str:
    """
    Break the main research question into structured sub-questions.
    """

    if not question.strip():
        return "⚠️ No research question provided."

    prompt = f"""
You are an expert research planner.

Your task:
Break the following research question into 3-5 clear, logical sub-questions.
Keep them concise and analytical.

Research Question:
{question}

Return the answer as a numbered list.
"""

    response = generate_response(prompt)

    if not response:
        return "⚠️ Planner agent failed to generate response."

    return response.strip()