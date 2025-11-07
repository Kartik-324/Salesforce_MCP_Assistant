"""
FastAPI Server - Using boss's MCP pattern
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.mcp_salesforce import SalesforceMCP
import asyncio

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize MCP
mcp = SalesforceMCP()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "✅ Salesforce MCP API (Boss's Pattern)"}


@app.get("/test")
async def test():
    """Test MCP connection"""
    try:
        result = await mcp.get_contacts_with_filter(limit=1)
        return {
            "status": "✅ MCP Connected",
            "data": result
        }
    except Exception as e:
        return {"status": "❌ Failed", "error": str(e)}


@app.post("/query")
async def query(request: QueryRequest):
    """Process query using MCP pattern"""
    q = request.query.lower()
    
    print(f"\n{'='*60}")
    print(f"📥 Query: {q}")
    print(f"{'='*60}")
    
    try:
        # View contacts
        if "contact" in q and "create" not in q:
            result = await mcp.get_all_contacts()
            
            if result and len(result) > 0:
                records = result[0].get("records", [])
                total = result[0].get("totalSize", 0)
                
                # Create readable response
                response_text = f"✅ Found {total} contacts (showing newest first)\n\n"
                
                # Show first 10 contacts
                for i, contact in enumerate(records[:10], 1):
                    # Handle both Name field and FirstName/LastName
                    name = contact.get("Name") or f"{contact.get('FirstName', '')} {contact.get('LastName', '')}".strip()
                    email = contact.get("Email", "No email")
                    phone = contact.get("Phone", "No phone")
                    title = contact.get("Title", "No title")
                    created = contact.get("CreatedDate", "")[:10] if contact.get("CreatedDate") else "N/A"
                    
                    response_text += f"{i}. {name}\n"
                    response_text += f"   📧 {email}\n"
                    response_text += f"   📞 {phone}\n"
                    response_text += f"   💼 {title}\n"
                    response_text += f"   📅 Created: {created}\n\n"
                
                if total > 10:
                    response_text += f"... and {total - 10} more contacts"
                
                return {
                    "response": response_text,
                    "data": {
                        "total": total,
                        "records": records
                    }
                }
        
        # View accounts
        elif "account" in q and "create" not in q:
            result = await mcp.get_accounts(limit=50)
            
            if result and len(result) > 0:
                records = result[0].get("records", [])
                total = result[0].get("totalSize", 0)
                
                # Create readable response
                response_text = f"✅ Found {total} accounts (showing newest first)\n\n"
                
                # Show first 10 accounts
                for i, account in enumerate(records[:10], 1):
                    name = account.get("Name", "N/A")
                    phone = account.get("Phone", "No phone")
                    industry = account.get("Industry", "N/A")
                    created = account.get("CreatedDate", "")[:10] if account.get("CreatedDate") else "N/A"
                    
                    response_text += f"{i}. {name}\n"
                    response_text += f"   📞 {phone}\n"
                    response_text += f"   🏢 {industry}\n"
                    response_text += f"   📅 Created: {created}\n\n"
                
                if total > 10:
                    response_text += f"... and {total - 10} more accounts"
                
                return {
                    "response": response_text,
                    "data": {
                        "total": total,
                        "records": records
                    }
                }
        
        # Create account
        elif "create" in q and "account" in q:
            words = q.split()
            name = "TestAccount"
            
            if "named" in words:
                idx = words.index("named") + 1
                if idx < len(words):
                    name = words[idx].capitalize()
            
            result = await mcp.create_account(name=name)
            
            if result and len(result) > 0:
                created_id = result[0].get("id", "Unknown")
                response_text = f"✅ Account Created Successfully!\n\n"
                response_text += f"📝 Name: {name}\n"
                response_text += f"🆔 ID: {created_id}\n"
                
                return {
                    "response": response_text,
                    "data": result[0] if result else {}
                }
        
        # Create contact
        elif "create" in q and "contact" in q:
            words = q.split()
            first = "Test"
            last = "Contact"
            
            if "named" in words:
                idx = words.index("named") + 1
                if idx < len(words):
                    first = words[idx].capitalize()
                if idx + 1 < len(words):
                    last = words[idx + 1].capitalize()
            
            result = await mcp.create_contact(
                first_name=first,
                last_name=last
            )
            
            if result and len(result) > 0:
                created_id = result[0].get("id", "Unknown")
                response_text = f"✅ Contact Created Successfully!\n\n"
                response_text += f"👤 Name: {first} {last}\n"
                response_text += f"🆔 ID: {created_id}\n"
                
                return {
                    "response": response_text,
                    "data": result[0] if result else {}
                }
        
        else:
            return {
                "response": "❓ Try: 'show contacts', 'show accounts', or 'create account named TechCorp'",
                "data": {}
            }
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            "response": f"❌ Error: {str(e)}",
            "data": {}
        }


@app.get("/list-tools")
async def list_tools():
    """List available MCP tools"""
    try:
        client = await mcp.initialize()
        tools = await client.list_tools()
        
        tool_list = [{"name": t.name, "description": t.description} for t in tools.tools]
        
        return {"tools": tool_list}
    except Exception as e:
        return {"error": str(e)}