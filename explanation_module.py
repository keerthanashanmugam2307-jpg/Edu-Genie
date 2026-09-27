from ai_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in very simple language for a beginner.

Topic:
{topic}

Structure your answer as:
1. Definition
2. How it works
3. Simple example
4. Key point to remember

Avoid complicated words.
"""
