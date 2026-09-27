from ai_client import generate_text


def create_learning_path(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Create a personalized learning path for a student who wants to learn:

{topic}

Include:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Suggested timeline
5. Practice activities
6. Useful learning resources

Keep the plan simple, practical, and easy to follow.
"""

    return generate_text(prompt)