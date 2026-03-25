import streamlit as st

from guardrails import semantic_guardrail, output_filter
from llm import get_llm_response

# -------- SESSION MEMORY --------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and safe AI assistant."}
    ]

# -------- LOGGING --------
def log_unsafe(input_text, reason):
    with open("logs/unsafe_logs.txt", "a") as f:
        f.write(f"{input_text} --> {reason}\n")

def count_logs():
    try:
        with open("logs/unsafe_logs.txt", "r") as f:
            return len(f.readlines())
    except:
        return 0


# -------- UI --------
st.title("🛡️ SafeLLM Guarded Chatbot")

st.info("Guardrails: Semantic Intent Detection + AI Safety + Output Filtering")

st.sidebar.title("📊 Unsafe Attempts")
st.sidebar.write(f"Total Blocked: {count_logs()}")

# -------- DISPLAY CHAT --------
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------- USER INPUT --------
user_input = st.chat_input("Enter your prompt")

# -------- MAIN LOGIC --------
if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # -------- SEMANTIC GUARDRAIL --------
    result = semantic_guardrail(user_input)

    # -------- MALICIOUS --------
    if result == "MALICIOUS":
        log_unsafe(user_input, "Malicious intent")

        with st.chat_message("assistant"):
            st.error("⚠️ Blocked: Malicious intent detected")
            st.warning("Risk Level: HIGH")

    # -------- SENSITIVE --------
    elif result == "SENSITIVE":
        with st.chat_message("assistant"):
            st.warning("⚠️ Risk Level: MEDIUM (Sensitive topic)")

            response = get_llm_response(st.session_state.messages)
            final_response = output_filter(response)

            st.session_state.messages.append(
                {"role": "assistant", "content": final_response}
            )

            st.write(final_response)

    # -------- SAFE --------
    else:
        with st.chat_message("assistant"):
            st.success("Risk Level: LOW")

            response = get_llm_response(st.session_state.messages)
            final_response = output_filter(response)

            st.session_state.messages.append(
                {"role": "assistant", "content": final_response}
            )

            st.write(final_response)