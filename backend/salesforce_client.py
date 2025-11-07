"""
Salesforce MCP Client - Following the boss's example pattern
Uses MCP SDK with ClientSession
"""
import asyncio
from typing import Optional
import json


class SalesforceMCPClient:
    """
    MCP Client for Salesforce following the example pattern
    This creates a simple MCP-like interface
    """
    
    def __init__(self, username: str, password: str, security_token: str, login_url: str):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.login_url = login_url
        
        # Import here to avoid issues if not installed
        from simple_salesforce import Salesforce
        
        # Initialize Salesforce connection
        # Extract domain from URL or use directly
        if "https://" in login_url:
            domain = login_url.replace("https://", "").replace(".salesforce.com", "")
        else:
            domain = login_url
        
        print(f"🔐 Connecting to Salesforce...")
        print(f"   Username: {username}")
        print(f"   Domain: {domain}")
        
        try:
            self.sf = Salesforce(
                username=username,
                password=password,
                security_token=security_token,
                domain=domain
            )
            print("✅ MCP Client initialized and connected to Salesforce\n")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            print("\nPlease verify:")
            print("1. Username is correct")
            print("2. Password is correct")
            print("3. Security token is valid (reset if needed)")
            print("4. Account is not locked")
            raise
    
    async def call_tool(self, tool_name: str, arguments: dict):
        """
        Call a tool (similar to session.call_tool in the example)
        This follows the MCP pattern
        """
        if tool_name == "query":
            return await self._execute_query(arguments.get("soql", ""))
        
        elif tool_name == "create":
            return await self._create_record(
                arguments.get("object"),
                arguments.get("fields", {})
            )
        
        elif tool_name == "update":
            return await self._update_record(
                arguments.get("object"),
                arguments.get("id"),
                arguments.get("fields", {})
            )
        
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
    
    async def _execute_query(self, soql: str):
        """Execute SOQL query"""
        # Run in executor to make it async
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.sf.query, soql)
        
        # Format response similar to MCP response
        class Content:
            def __init__(self, text):
                self.text = text
        
        class ToolResult:
            def __init__(self, content):
                self.content = content
        
        # Format the result
        formatted_result = {
            "totalSize": result["totalSize"],
            "records": result["records"]
        }
        
        content = Content(json.dumps(formatted_result, indent=2))
        return ToolResult([content])
    
    async def _create_record(self, obj_type: str, fields: dict):
        """Create a record"""
        loop = asyncio.get_event_loop()
        
        # Get the object
        sf_object = getattr(self.sf, obj_type)
        result = await loop.run_in_executor(None, sf_object.create, fields)
        
        class Content:
            def __init__(self, text):
                self.text = text
        
        class ToolResult:
            def __init__(self, content):
                self.content = content
        
        formatted_result = {
            "success": True,
            "id": result["id"],
            "message": f"Created {obj_type} successfully"
        }
        
        content = Content(json.dumps(formatted_result, indent=2))
        return ToolResult([content])
    
    async def _update_record(self, obj_type: str, record_id: str, fields: dict):
        """Update a record"""
        loop = asyncio.get_event_loop()
        
        # Get the object and update
        sf_object = getattr(self.sf, obj_type)
        await loop.run_in_executor(None, sf_object.update, record_id, fields)
        
        class Content:
            def __init__(self, text):
                self.text = text
        
        class ToolResult:
            def __init__(self, content):
                self.content = content
        
        formatted_result = {
            "success": True,
            "id": record_id,
            "message": f"Updated {obj_type} successfully"
        }
        
        content = Content(json.dumps(formatted_result, indent=2))
        return ToolResult([content])
    
    async def list_tools(self):
        """
        List available tools (like session.list_tools() in the example)
        """
        class Tool:
            def __init__(self, name, description):
                self.name = name
                self.description = description
        
        class ToolsList:
            def __init__(self, tools):
                self.tools = tools
        
        tools = [
            Tool("query", "Execute SOQL query on Salesforce"),
            Tool("create", "Create a new record in Salesforce"),
            Tool("update", "Update an existing record in Salesforce")
        ]
        
        return ToolsList(tools)