from llm.ollama_client import generate_response


def generate_hypothesis(context: str) -> str:
    """
    Generate hypothesis and future research directions
    based strictly on provided research analysis.
    """

    if not context or "⚠️" in context:
        return "⚠️ No valid analysis context available for hypothesis generation."

    prompt = f"""
You are a scientific research strategist.

Based ONLY on the following research analysis,
generate logical and realistic research extensions.

------------------------
Research Analysis:
{context}
------------------------

Provide output in this format:

1. Core Research Hypothesis
2. Supporting Rationale
3. Experimental Design Ideas
4. Evaluation Metrics Suggestions
5. Future Research Directions

Be analytical and avoid speculation beyond the given analysis.
"""

    response = generate_response(prompt)

    if not response:
        return "⚠️ Hypothesis agent failed to generate response."

    return response.strip()