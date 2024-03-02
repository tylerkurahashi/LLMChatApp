import streamlit as st

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
    response = "こんにちは"
    st.markdown(response)
    
  st.session_state.messages.append({"role": "assistant", "content": response})