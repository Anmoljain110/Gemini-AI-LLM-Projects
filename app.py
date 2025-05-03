# load env file
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Supportive model
model = genai.GenerativeModel("gemini-2.0-flash-001")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="Q&A demo")

st.header("Gemini LLM Application")

input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit:
    response= get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)