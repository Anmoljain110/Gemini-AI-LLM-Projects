from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.0-flash-001")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit Interface
st.set_page_config(page_title="Gemini LLM App")
st.header("Ask Gemini")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Enter your question:", key="input")
submit = st.button("Ask")

if submit and input:
    answer = get_gemini_response(input)
    st.session_state.chat_history.append(("You", input))
    st.session_state.chat_history.append(("Gemini", answer))

    st.subheader("Answer:")
    st.write(answer)

st.subheader("Chat History:")
for role, msg in st.session_state.chat_history:
    st.write(f"{role}: {msg}")
