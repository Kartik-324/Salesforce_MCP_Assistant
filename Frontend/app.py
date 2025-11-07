"""
Streamlit Frontend for MCP Salesforce
"""
import streamlit as st
import requests
import json

st.set_page_config(page_title="Salesforce MCP", page_icon="🤖", layout="wide")

st.title("🤖 Salesforce MCP Assistant")
st.markdown("**Using Official MCP SDK Protocol**")

# Sidebar
with st.sidebar:
    st.header("💡 Try These")
    st.markdown("""
    - Show me contacts
    - List accounts
    - Create account named TechCorp
    """)
    
    st.markdown("---")
    st.header("🔧 MCP Status")
    
    if st.button("Test MCP Connection"):
        try:
            response = requests.get("http://127.0.0.1:8000/test")
            if response.status_code == 200:
                data = response.json()
                st.success(data.get("status", "Connected"))
            else:
                st.error("❌ MCP not responding")
        except:
            st.error("❌ Cannot connect")

API_URL = "http://127.0.0.1:8000/query"

# Quick actions
col1, col2 = st.columns(2)
with col1:
    if st.button("📇 Show Contacts", use_container_width=True):
        st.session_state.query = "show contacts"

with col2:
    if st.button("🏢 Show Accounts", use_container_width=True):
        st.session_state.query = "show accounts"

# Main input
query = st.text_input(
    "Ask about Salesforce data:",
    value=st.session_state.get("query", ""),
    placeholder="e.g., show me all contacts"
)

if st.button("Submit", type="primary") or query:
    if query.strip():
        with st.spinner("🔄 Querying via MCP..."):
            try:
                response = requests.post(API_URL, json={"query": query}, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.subheader("💬 Response:")
                    st.success(result.get("response", "No response"))
                    
                    # Show data
                    if result.get("data"):
                        with st.expander("📊 View Data", expanded=True):
                            st.json(result["data"])
                        
                        # Download JSON
                        json_str = json.dumps(result, indent=2)
                        st.download_button(
                            "📥 Download JSON",
                            data=json_str,
                            file_name="mcp_result.json",
                            mime="application/json"
                        )
                else:
                    st.error(f"❌ Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a query")

st.markdown("---")
st.markdown("💡 **Using Official MCP SDK:** `mcp` + `@modelcontextprotocol/server-salesforce`")