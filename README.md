# 🤖 Salesforce MCP Assistant  
### *End-to-End Salesforce Automation using MCP, FastAPI, and Streamlit*

---

## 🚀 Overview

**Salesforce MCP Assistant** is a full-stack intelligent assistant that connects to Salesforce using the **Model Context Protocol (MCP)**.  
It lets you **query, create, and manage Salesforce records** through a **Streamlit UI** backed by a **FastAPI server**.

The app follows a clean modular structure — separating the **frontend**, **backend**, and **Salesforce MCP client** — making it easy to extend with **LangChain**, **OpenAI**, or other LLMs.

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
└── .env # (ignored for security)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kartik-324/Salesforce_MCP_Assistant.git
cd Salesforce_MCP_Assistant
2️⃣ Create and Activate a Virtual Environment
Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Setup Environment Variables
Create a .env file in the root directory and add your credentials:

bash
Copy code
SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_TOKEN=your_security_token
OPENAI_API_KEY=your_openai_api_key
5️⃣ Run the Backend (FastAPI)
bash
Copy code
cd backend
uvicorn main:app --reload
6️⃣ Run the Frontend (Streamlit)
bash
Copy code
cd frontend
streamlit run app.py
🧩 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	FastAPI
Integration	Salesforce MCP
AI Framework	LangChain / OpenAI
Language	Python

📌 Features
✅ End-to-end Salesforce automation via MCP
✅ Modular architecture for scalability
✅ Environment-based configuration for security
✅ Easy integration with any LLM or API
✅ Interactive Streamlit frontend

👨‍💻 Author
Kartik Joshi
🔗 GitHub Profile
📧 Feel free to contribute or open issues!

