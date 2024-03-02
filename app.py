import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from const import OPENAI_API_MODEL, OPENAI_API_TEMPERATURE

load_dotenv()

st.title("llm-chat-app")

if "messages" not in st.session_state:
  st.session_state.messages = []
  
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
    
prompt = st.chat_input("What is up?")

if prompt:
  st.session_state.messages.append({"role": "user", "content": prompt})
  
  with st.chat_message("user"):
    st.markdown(prompt)
    
  with st.chat_message("assistant"):
    chat = ChatOpenAI(
      model=OPENAI_API_MODEL,
      temperature=OPENAI_API_TEMPERATURE
    )
    messages = [HumanMessage(content=prompt)]
    response = chat(messages)
    st.markdown(response.content)
    
  st.session_state.messages.append({"role": "assistant", "content": response})