from ai_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following text for a student.

Text:
{text}

Give:
1. A short summary
2. Important points
3. Key terms to remember

Keep it clear, simple, and useful for revision.
"""

    return generate_text(prompt)