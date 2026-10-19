from main import vedio_process
import cv2
import streamlit as st

st.set_page_config(page_title="Sign Language Chatbot", layout="wide")

st.title("🤖 Sign Language Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Layout
col1, col2 = st.columns([2,1])

with col1:
    st.subheader("📷 Camera Input")
    frame_window = st.image([])

with col2:
    st.subheader("💬 Chat")

    chat_container = st.container()

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

# Start Camera
run = st.checkbox("Start Camera")

cap = cv2.VideoCapture(0)

while run:
    
    ret, frame = cap.read()

    if not ret:
        st.write("Camera Error")
        break

    frame, letter, confidence, sentence, user_text, bot_responce = vedio_process(frame)

    cv2.rectangle(frame,(300,100),(600,400),(0,255,0),2)

    cv2.putText(frame, sentence, (50,200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_window.image(frame)

    if user_text:
        st.session_state.messages.append({
            "role":"user",
            "content":user_text
        })

    if bot_responce:
        st.session_state.messages.append({
            "role":"assistant",
            "content":bot_responce
        })

cap.release()
cv2.destroyAllWindows()