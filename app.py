import streamlit as st
from pymongo import MongoClient
import bcrypt
import pdfplumber
import requests

# MOCKED DATABASE (for local UI testing without Docker)
class MockCollection:
    def __init__(self):
        self.data = []
    def find_one(self, query):
        for item in self.data:
            if all(item.get(k) == v for k, v in query.items()):
                return item
        return None
    def insert_one(self, doc):
        self.data.append(doc)

if "mock_users" not in st.session_state:
    st.session_state.mock_users = MockCollection()
if "mock_docs" not in st.session_state:
    st.session_state.mock_docs = MockCollection()

users = st.session_state.mock_users
docs = st.session_state.mock_docs

#To use MongoDB uncomment the following lines and comment out the above lines
#client = MongoClient("mongodb://mongodb:27017/")
#db = client["ai_app"]
#users = db["users"]
#docs = db["documents"]
#users = MockCollection()
#docs = MockCollection()

if "user" not in st.session_state:
    st.session_state.user = ""
if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="DocuMind AI", layout="wide", page_icon="📄")

st.markdown("""
<style>
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: gray;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 100;
    }
</style>
""", unsafe_allow_html=True)

def hash_password(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

def check_password(pw, hashed):
    return bcrypt.checkpw(pw.encode(), hashed)

def auth_page():
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>DocuMind AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: gray;'>Your intelligent document analysis assistant.</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Login", use_container_width=True):
                user = users.find_one({"username": u})
                if user and check_password(p, user["password"]):
                    st.session_state.user = u
                    st.session_state.history = []
                    st.rerun()
                else:
                    st.error("Invalid credentials")

        with tab2:
            ru = st.text_input("New Username")
            rp = st.text_input("New Password", type="password")
            if st.button("Register", use_container_width=True):
                if users.find_one({"username": ru}):
                    st.error("User exists")
                else:
                    users.insert_one({"username": ru, "password": hash_password(rp)})
                    st.success("Registered")

def chat_page():
    st.title("DocuMind AI- Ai Assisted Document Chatbot")

    with st.sidebar:
        st.markdown(f"### Welcome, **{st.session_state.user}** 👋")
        if st.button("Logout", use_container_width=True):
            st.session_state.user = ""
            st.session_state.history = []
            st.rerun()
            
        st.divider()
        st.markdown("### 📄 Document Analysis")
        file = st.file_uploader("Upload PDF to analyze", type="pdf", label_visibility="collapsed")
        if file:
            text = ""
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            docs.insert_one({"user": st.session_state.user, "content": text})
            st.success("PDF processed successfully! 🎉")

    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    q = st.chat_input("Ask something")

    if q:
        st.session_state.history.append({"role": "user", "content": q})

        doc = docs.find_one({"user": st.session_state.user})
        if not doc:
            ans = "Upload PDF first"
        else:
            content = doc["content"][:3000]
            res = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": "Bearer ...",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": [
                        {"role": "system", "content": "Answer based on context"},
                        {"role": "user", "content": content + "\nQuestion: " + q}
                    ]
                }
            )
            try:
                ans = res.json()["choices"][0]["message"]["content"]
            except:
                ans = res.text

        st.session_state.history.append({"role": "assistant", "content": ans})
        st.rerun()

if st.session_state.user:
    chat_page()
else:
    auth_page()

st.markdown('<div class="footer">Crafted with ❤️ by Apoorv Sharma</div>', unsafe_allow_html=True)