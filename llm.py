import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_llm_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a safe and responsible AI assistant.

Rules:
- Provide clear, complete, and concise answers (120–180 words)
- Do NOT provide step-by-step harmful or illegal instructions
- If topic is sensitive (e.g., hacking), explain concepts only
- Focus on educational and defensive perspective
"""
            }
        ] + messages,
        max_tokens=400
    )

    return response.choices[0].message.content