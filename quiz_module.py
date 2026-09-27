import json
from ai_client import generate_text


def generate_quiz(topic: str):
    prompt = f"""
Create a quiz for a student about this topic:

{topic}

Create exactly 3 multiple-choice questions.

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Correct option"
  }}
]

Rules:
- Exactly 3 questions
- Exactly 4 options for each question
- One correct answer for each question
- No Markdown
- No extra text outside the JSON
"""

    result = generate_text(prompt).strip()

    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    try:
        quiz = json.loads(result)
    except json.JSONDecodeError:
        raise ValueError("Gemini returned invalid quiz JSON.")

    if not isinstance(quiz, list) or len(quiz) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for item in quiz:
        if not all(key in item for key in ["question", "options", "answer"]):
            raise ValueError("Invalid quiz format.")

        if len(item["options"]) != 4:
            raise ValueError("Each question must have exactly 4 options.")

    return quiz