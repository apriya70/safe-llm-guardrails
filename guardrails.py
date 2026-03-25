import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def semantic_guardrail(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a safety classifier.

Classify the user input into ONE of these categories:

SAFE → harmless, informational queries  
SENSITIVE → cybersecurity, hacking concepts, but educational  
MALICIOUS → requests for illegal, harmful, or unethical actions  

Rules:
- "what is hacking" → SENSITIVE  
- "explain jailbreak" → SENSITIVE  
- "how to hack wifi" → MALICIOUS  
- "how to bypass system security" → MALICIOUS  

Return ONLY one word:
SAFE / SENSITIVE / MALICIOUS
"""
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=5
    )

    return response.choices[0].message.content.strip().upper()


def output_filter(response):
    blocked = ["explosive", "weapon"]

    for word in blocked:
        if word in response.lower():
            return "⚠️ Response blocked due to unsafe content"

    return response