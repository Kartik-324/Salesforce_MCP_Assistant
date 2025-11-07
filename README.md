# 🤖 Salesforce MCP Assistant  
### End-to-End Salesforce Automation using MCP, FastAPI, and Streamlit  

---

## 🚀 Overview  

**Salesforce MCP Assistant** is a full-stack intelligent assistant that connects to Salesforce using the **Model Context Protocol (MCP)**.  
It lets you query, create, and manage Salesforce records through a **Streamlit UI** backed by a **FastAPI** server.  

The app follows a clean modular structure — separating the frontend, backend, and Salesforce MCP client —  
making it easy to extend with LangChain, OpenAI, or other LLMs.

---

## 🧱 Project Structure  

<pre> ```bash Salesforce_MCP_Assistant/ │ ├── backend/ │ ├── main.py # FastAPI server │ ├── mcp_salesforce.py # MCP wrapper to process queries │ └── salesforce_client.py # Salesforce MCP client implementation │ ├── frontend/ │ └── app.py # Streamlit-based frontend │ ├── requirements.txt ├── .gitignore ├── README.md └── .env # (ignored for security) ``` </pre>


---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Kartik-324/Salesforce_MCP_Assistant.git
cd Salesforce_MCP_Assistant
2️⃣ Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # Windows
or

bash
Copy code
source venv/bin/activate   # macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Run the Application
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
Once both servers are running:
👉 Open your browser at http://localhost:8501 to access the Streamlit interface.

🔍 Example Queries
“Show me all Salesforce contacts”

“List accounts with revenue above 1M”

“Create account named TechCorp”

“Get details of opportunities closed this month”

🧩 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	FastAPI
Integration	Model Context Protocol (MCP)
Language	Python
API Calls	Salesforce REST API
LLM Ready	LangChain / OpenAI compatible

🛡️ Environment Variables
Make a .env file in the project root with your credentials:

ini
Copy code
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_TOKEN=your_token

🧠 Powered By
Model Context Protocol (MCP)
FastAPI • Streamlit • LangChain Compatible
