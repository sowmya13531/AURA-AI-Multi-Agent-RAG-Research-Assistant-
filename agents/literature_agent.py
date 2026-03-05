from llm.ollama_client import generate_response


def analyze_literature(context: str, question: str) -> str:
    """
    Analyze retrieved literature context with respect to the research question.
    """

    if not question.strip():
        return "⚠️ No question provided for literature analysis."

    if not context or "⚠️" in context:
        return "⚠️ No valid context available for literature analysis."

    prompt = f"""
You are a research literature review expert.

Use ONLY the provided context to analyze the research question.
Do not hallucinate or add external information.

--------------------
Context:
{context}
--------------------

Research Question:
{question}

Provide structured output in this format:

1. Key Findings
2. Important Methods or Approaches
3. Limitations Identified
4. Research Gaps
5. Summary
"""

    response = generate_response(prompt)

    if not response:
        return "⚠️ Literature agent failed to generate response."

    return response.strip()