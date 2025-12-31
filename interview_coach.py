import streamlit as st
import random
import time

st.set_page_config(page_title="MS Interview Coach", page_icon="👔")

st.title("👔 Microsoft Interview Coach")
st.write("Practice your interview skills with this local Rule-Based AI.")

# --- THE KNOWLEDGE BASE ---
# This is the "Brain" of your AI. You can add as many as you want!
BRAIN = {
    "python": "Microsoft uses Python for AI and Cloud. Make sure you know about lists, dictionaries, and decorators!",
    "culture": "Microsoft values a 'Growth Mindset.' They want people who are curious and learn from mistakes.",
    "projects": "When talking about projects, use the STAR method: Situation, Task, Action, and Result.",
    "azure": "Azure is Microsoft's cloud platform. It's a huge part of their business!",
    "hi": "Hello! I am your interview coach. Ask me about Microsoft culture, Python, or how to describe your projects.",
    "help": "You can ask me about: 'python', 'culture', 'projects', or 'Azure'."
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask me a question about Microsoft..."):
    # 1. Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Logic: Search the brain for keywords
    response = "That's a great question! I don't have a specific tip for that yet, but try asking about 'Python' or 'Culture'."
    
    # Check if any of our "Brain" keys are inside the user's prompt
    user_text = prompt.lower()
    for key in BRAIN:
        if key in user_text:
            response = BRAIN[key]
            break

    # 3. Add AI response with a tiny "thinking" delay to make it feel real
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
