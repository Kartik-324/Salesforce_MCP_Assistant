# 🤖 Salesforce MCP Assistant  
### End-to-End Salesforce Automation using MCP, FastAPI, and Streamlit  

---

## 🚀 Overview  

**Salesforce MCP Assistant** is an intelligent full-stack AI assistant that enables seamless interaction with Salesforce using the **Model Context Protocol (MCP)**.  
It allows users to query, create, update, and manage Salesforce records using natural language through a clean **Streamlit UI**, powered by a robust **FastAPI** backend.

The system follows a modular and scalable architecture, separating frontend, backend, and Salesforce MCP logic.  
It is designed to be **LLM-ready**, making it easy to integrate with LangChain, OpenAI, or other AI frameworks for advanced automation and reasoning.

---

## ✨ Key Features  

- 🤖 Natural language interaction with Salesforce  
- 🔗 Salesforce integration via Model Context Protocol (MCP)  
- ⚡ FastAPI backend for scalable API handling  
- 🖥️ Streamlit-based interactive frontend  
- 🧠 LLM-ready architecture (LangChain / OpenAI compatible)  
- 🧩 Modular and extensible project structure  
- 🔐 Secure environment-based credential management  

---

## 🧱 Project Structure  

Salesforce_MCP_Assistant/
│
├── backend/
│ ├── main.py # FastAPI server
│ ├── mcp_salesforce.py # MCP wrapper to process queries
│ └── salesforce_client.py # Salesforce MCP client implementation
│
├── frontend/
│ └── app.py # Streamlit-based frontend
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env # Ignored for security

yaml
Copy code

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Kartik-324/Salesforce_MCP_Assistant.git
cd Salesforce_MCP_Assistant
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
macOS / Linux

bash
Copy code
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Running the Application
🧠 Start Backend (FastAPI)
bash
Copy code
cd backend
uvicorn main:app --reload
💻 Start Frontend (Streamlit)
bash
Copy code
cd ../frontend
streamlit run app.py
Once both servers are running, open your browser at:
👉 http://localhost:8501

🔍 Example Queries
“Show me all Salesforce contacts”

“List accounts with revenue above 1M”

“Create an account named TechCorp”

“Get opportunities closed this month”

🧩 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	FastAPI
Integration	Model Context Protocol (MCP)
Language	Python
API	Salesforce REST API
AI Ready	LangChain / OpenAI Compatible

🛡️ Environment Variables
Create a .env file in the project root:

ini
Copy code
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_TOKEN=your_security_token
⚠️ Do not commit .env to GitHub

🧠 Powered By
Model Context Protocol (MCP)

FastAPI

Streamlit

LangChain (Optional Integration)

📌 Future Enhancements
🔄 Support for update & delete operations

🧠 Advanced LLM reasoning with LangGraph

📊 Analytics dashboard for Salesforce data

🔐 OAuth-based authentication

