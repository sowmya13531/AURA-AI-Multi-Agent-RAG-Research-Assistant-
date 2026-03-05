from llm.ollama_client import generate_response


def write_report(question: str, analysis: str, hypothesis: str) -> str:
    """
    Generate a complete structured research-style report.
    """

    if not question.strip():
        return "⚠️ No research question provided."

    if not analysis or "⚠️" in analysis:
        return "⚠️ Literature analysis missing or invalid."

    if not hypothesis or "⚠️" in hypothesis:
        return "⚠️ Hypothesis generation missing or invalid."

    prompt = f"""
You are an academic research paper writer.

Using the provided information, write a clear,
formal, well-structured research report.

------------------------
Research Question:
{question}

Literature Analysis:
{analysis}

Hypothesis & Research Ideas:
{hypothesis}
------------------------

Structure the report as follows:

1. Abstract (concise summary)
2. Introduction (background and importance)
3. Literature Analysis Summary
4. Proposed Methodology
5. Expected Outcomes
6. Future Work
7. Conclusion

Write in formal academic tone.
Do not invent external references.
Base everything strictly on the provided content.
"""

    response = generate_response(prompt)

    if not response:
        return "⚠️ Writer agent failed to generate report."

    return response.strip()