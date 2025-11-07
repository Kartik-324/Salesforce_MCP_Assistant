🤖 Salesforce MCP Assistant
End-to-End Salesforce Automation using MCP, FastAPI, and Streamlit

🚀 Overview

Salesforce MCP Assistant is a full-stack intelligent assistant that connects to Salesforce using the Model Context Protocol (MCP).
It lets you query, create, and manage Salesforce records through a Streamlit UI backed by a FastAPI server.

The app follows a clean modular structure — separating the frontend, backend, and Salesforce MCP client — making it easy to extend with LangChain, OpenAI, or other LLMs.

🏗️ Project Structure
Salesforce_MCP_Assistant/
│
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── mcp_salesforce.py       # MCP wrapper to process queries
│   ├── salesforce_client.py    # Salesforce MCP client implementation
│
├── frontend/
│   ├── app.py                  # Streamlit-based frontend
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env                        # (ignored for security)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Kartik-324/Salesforce_MCP_Assistant.git
cd Salesforce_MCP_Assistant

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables

Create a file named .env in the project root with:

SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_SECURITY_TOKEN=your_security_token
SALESFORCE_DOMAIN=https://login.salesforce.com

OPENAI_API_KEY=your_openai_api_key   # optional for LLM support


🛑 Note: .env is in .gitignore — never commit your credentials.

▶️ Running the Project
🧠 Start the Backend (FastAPI)
cd backend
uvicorn main:app --reload


Server runs at: http://127.0.0.1:8000

💻 Start the Frontend (Streamlit)

In a new terminal:

cd frontend
streamlit run app.py


App runs at: http://localhost:8501

🧩 Features

✅ Query Salesforce via MCP SDK
✅ Streamlit frontend for quick testing
✅ Create, Update, and List records
✅ LLM integration ready (LangChain/OpenAI)
✅ Secure .env usage with git protection

🧠 Example Queries
Command	What It Does
show contacts	Fetches contact records from Salesforce
show accounts	Lists Salesforce accounts
create account named TechCorp	Creates a new Account
create contact named John Doe	Adds a new Contact
📊 Example Response
{
  "totalSize": 3,
  "records": [
    {
      "Id": "0039F00004QmZTqQAN",
      "Name": "John Doe",
      "Email": "john@example.com"
    }
  ]
}

🧱 MCP Architecture
Layer	Description
salesforce_client.py	Connects to Salesforce and executes SOQL queries
mcp_salesforce.py	Implements MCP tool interface (query/create/update)
main.py	FastAPI layer exposing HTTP endpoints
app.py	Streamlit UI calling the FastAPI routes
🌟 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	FastAPI
API SDK	Simple-Salesforce
Protocol	MCP (Model Context Protocol)
Language	Python 3.10+
🔮 Future Plans

🧠 Add LangChain + LLM query understanding

🧾 Add record filtering and analytics dashboard

📈 Integrate Leads and Opportunities modules

🪪 License

This project is licensed under the MIT License.

👨‍💻 Author

Kartik Joshi
📧 For queries: GitHub Profile → @Kartik-324
