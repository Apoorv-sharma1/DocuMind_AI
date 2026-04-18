# 📄 DocuMind AI — Intelligent PDF Q&A System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> Transform static PDFs into interactive, AI-powered conversations.

---

## 🚀 Overview

**DocuMind AI** is a full-stack AI-powered document assistant that allows users to upload PDFs and ask questions in natural language. It intelligently processes, stores, retrieves, and generates context-aware answers using advanced LLMs.

---

## ✨ Features

- 🔐 Secure User Authentication (Register/Login)
- 📂 Upload and parse PDF documents
- 🧠 AI-powered document understanding
- 💬 Chat-based question-answering interface
- ⚡ Fast responses using Groq API (LLaMA 3)
- 🗄️ MongoDB storage for users and documents
- 🔄 Session management for seamless UX
- 🌐 Clean and interactive UI with Streamlit
- 🐳 Docker support for easy deployment

---

## 🧠 How It Works

```mermaid
flowchart LR
A[User Opens App] --> B[Login/Register]
B --> C[Session Created]
C --> D[Upload PDF]
D --> E[Extract Text]
E --> F[Store in MongoDB]
F --> G[Ask Question]
G --> H[Fetch Relevant Data]
H --> I[Send to LLM]
I --> J[Generate Answer]
J --> K[Display Response]
```

---

## 🛠️ Tech Stack

| Layer        | Technology Used |
|-------------|----------------|
| Frontend     | Streamlit |
| Backend      | Python |
| Database     | MongoDB |
| Authentication | bcrypt |
| PDF Parsing  | pdfplumber |
| AI Model     | Groq API (LLaMA 3) |
| Deployment   | Docker |

---

## 📸 Screenshots

### 🔐 Login Page
![Login Screenshot](screenshots/login.png)

### 📂 Upload PDF
![Upload Screenshot](screenshots/upload.png)

### 💬 Chat Interface
![Chat Screenshot](screenshots/chat.png)

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites

- Python 3.10+
- MongoDB (local or Atlas)
- Groq API Key
- Docker (optional)

---

### 📥 Clone Repository

```bash
git clone https://github.com/your-username/documind-ai.git
cd documind-ai
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
GROQ_API_KEY=your_groq_api_key
```

---

### ▶️ Run the Application

```bash
streamlit run app.py
```

App will run on:

```
http://localhost:8501
```

---

## 🐳 Docker Setup (Optional)

```bash
docker build -t documind-ai .
docker run -p 8501:8501 documind-ai
```

---

## 📌 Project Structure

```
documind-ai/
│── app.py
│── requirements.txt
│── Dockerfile
│── .env
│── utils/
│   ├── auth.py
│   ├── db.py
│   ├── pdf_parser.py
│   ├── llm.py
│── screenshots/
│── README.md
```

---

## 📚 Use Cases

- 📖 Study & research assistant  
- ⚖️ Legal document analysis  
- 📊 Business reports Q&A  
- 🧾 Resume & content understanding  
- 🧠 Personal knowledge base  

---

## 🔮 Future Improvements

- 🔍 Semantic search (vector DB integration)
- 📊 Multi-document querying
- 🌐 Web-based frontend (React)
- 🧠 Memory-based conversations
- 📱 Mobile-friendly UI

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repo
# Create a new branch
git checkout -b feature-name

# Commit changes
git commit -m "Added new feature"

# Push
git push origin feature-name
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Apoorv Sharma**  
🚀 AI & Automation Enthusiast  
🌐 Building @ FuseOne Studios

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repo  
- 🍴 Fork it  
- 📢 Share with others
