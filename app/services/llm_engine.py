import requests
from app.core.config import GROQ_API_KEY, GROQ_URL

def evaluate_with_llm(prompt: str):

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
You are a strict JSON generator.

Evaluate the following prompt for prompt engineering quality.

Prompt: {prompt}

Return ONLY valid JSON in this exact format:
{{
  "score": 1-10,
  "clarity": "short sentence",
  "improvement": "short suggestion"
}}

Do NOT include:
- explanations
- markdown
- extra text
- headings

ONLY JSON.
"""
                }
            ]
        }

        response = requests.post(GROQ_URL, headers=headers, json=data)

        result = response.json()

        print("GROQ RESPONSE:", result)

        if "choices" not in result:
            return '{"score": 5, "clarity": "LLM failed", "improvement": "Try again"}'

        content = result["choices"][0]["message"]["content"]

        return content

    except Exception as e:
        print("LLM ERROR:", str(e))
        return '{"score": 5, "clarity": "Error occurred", "improvement": "Try again"}'