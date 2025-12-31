import streamlit as st
import time

# 1. Page Setup
st.set_page_config(page_title="Interview Coach", page_icon="🎤")
st.title("🎤 Interview Coach")

# 2. Initialize the "Teachable Brain" in Session State
if "brain" not in st.session_state:
    st.session_state.brain = {
        "hello": "Hi there! I'm your interview coach. Teach me something new in the sidebar!",
        "python": "Python is vital for data roles. Focus on Pandas and NumPy.",
        "star": "Use the STAR method: Situation, Task, Action, Result."
    }

# 3. Sidebar: The "Teaching" Center
with st.sidebar:
    st.header("🧠 Teach the AI")
    new_keyword = st.text_input("When I say...").lower()
    new_response = st.text_area("You should say...")
    
    if st.button("Add to Memory"):
        if new_keyword and new_response:
            st.session_state.brain[new_keyword] = new_response
            st.success(f"Learned: '{new_keyword}'")
        else:
            st.error("Please fill both boxes!")

    st.divider()
    st.write("Current Memory Size:", len(st.session_state.brain))

# 4. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question or test a keyword..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Logic: Search the brain for keywords
    bot_reply = "I haven't learned about that yet. Can you teach me in the sidebar?"
    user_text = prompt.lower()
    
    for key, response in st.session_state.brain.items():
        if key in user_text:
            bot_reply = response
            break

    # Simulate "Thinking"
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for word in bot_reply.split():
            full_response += word + " "
            time.sleep(0.05)
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
