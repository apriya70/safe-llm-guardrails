# SafeLLM Guardrails System
LLM safety system with semantic guardrails for detecting malicious and sensitive prompts in real-time.

## 1. Overview
- SafeLLM is a semantic guardrail system designed to improve the safety and reliability of Large Language Models.
- It uses LLM-based classification to detect harmful, sensitive, and malicious inputs instead of keyword filtering.

## 2. Problem Statement
- LLMs can generate unsafe outputs when exposed to malicious prompts or prompt injection attacks.
- This project adds a guardrail layer to prevent misuse while maintaining usability.

## 3. Approach
- Hybrid architecture including:
  - LLM-based intent classification (SAFE, SENSITIVE, MALICIOUS)
  - Prompt injection detection
  - Controlled response generation
  - Output filtering

## 4. Architecture
- User Input → Guardrail → Decision → LLM → Output Filter → Response

## 5. Features
- Context-aware intent detection
- Prompt injection protection
- Risk classification (Low, Medium, High)
- Chat memory support
- Logging of unsafe inputs

## 6. Tech Stack
- Python
- Streamlit
- OpenAI API (gpt-4o-mini)

## 7. Setup

### 7.1 Clone the repository
git clone https://github.com/apriya70/safe-llm-guardrails.git

cd safe-llm-guardrails

### 7.2 Install dependencies
pip install -r requirements.txt

### 7.3 Configure environment variables
# Create a .env file and add:
OPENAI_API_KEY=your_key_here

### 7.4 Run the application
streamlit run app.py

## 8. Key Insight
- LLM-based semantic classification provides better robustness and contextual understanding compared to keyword-based filtering.

## 9. Future Work
- Fine-tuned safety models
- Logging dashboard
- Multi-language support
