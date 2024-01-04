import openai
import streamlit as st
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Audio Story generator") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Story is being generated"}]



if prompt := st.button("Generate"):

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    msg =  st.session_state["messages"] #"Write a story no more than 500 words"
    st.chat_message(msg["role"]).write(msg['content'])
    openai.api_key = openai_api_key
    msg.append({"role": "user", "content": "Write a story no more than 500 words"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msg)
    msg = response.choices[0].message
    st.chat_message("assistant").write(msg.content)

