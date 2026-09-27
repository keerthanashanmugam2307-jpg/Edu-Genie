from ai_client import generate_text


def answer_question(question: str) -> str:
    if not question or not question.strip():
        return "Please enter a valid question."

    prompt = f"""
You are EduGenie, a friendly educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Give:
1. A simple direct answer
2. A short explanation
3. One simple example if useful

Use beginner-friendly language.
"""

    try:
        return generate_text(prompt)
    except Exception as e:
        return (
            "I couldn't generate an answer right now. "
            "Please check your Gemini API key in the .env file. "
            f"Details: {e}"
        )