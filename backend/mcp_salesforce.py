"""
Salesforce MCP Wrapper - Following boss's example pattern
"""
import asyncio
from backend.salesforce_client import SalesforceMCPClient
import os
from dotenv import load_dotenv
import json

load_dotenv()


class SalesforceMCP:
    """
    Main MCP interface following the example pattern
    Simulates: async with ClientSession(read, write) as session
    """
    
    def __init__(self):
        self.username = os.getenv("SALESFORCE_USERNAME")
        self.password = os.getenv("SALESFORCE_PASSWORD")
        self.security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")
        self.login_url = os.getenv("SALESFORCE_DOMAIN", "https://login.salesforce.com")
        
        if not all([self.username, self.password, self.security_token]):
            raise ValueError("Missing Salesforce credentials in .env")
        
        self.client = None
    
    async def initialize(self):
        """Initialize the MCP client (like session.initialize())"""
        self.client = SalesforceMCPClient(
            username=self.username,
            password=self.password,
            security_token=self.security_token,
            login_url=self.login_url
        )
        return self.client
    
    async def get_all_contacts(self):
        """
        Get all contacts - Following boss's example pattern
        """
        client = await self.initialize()
        
        # List available tools (like in the example)
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools.tools:
            print(f"  - {tool.name}")
        
        # Query contacts using SOQL - ORDER BY CreatedDate DESC to show newest first
        query_result = await client.call_tool(
            "query",
            arguments={
                "soql": "SELECT Id, FirstName, LastName, Name, Email, Phone, Title, CreatedDate FROM Contact ORDER BY CreatedDate DESC LIMIT 50"
            }
        )
        
        # Process results (like in the example)
        data = []
        for content in query_result.content:
            if hasattr(content, 'text'):
                data.append(json.loads(content.text))
        
        return data
    
    async def get_contacts_with_filter(self, limit=100):
        """
        Get contacts with filter - Following boss's example
        """
        client = await self.initialize()
        
        query_result = await client.call_tool(
            "query",
            arguments={
                "soql": f"SELECT Id, FirstName, LastName, Name, Email, Phone, Title, CreatedDate FROM Contact ORDER BY CreatedDate DESC LIMIT {limit}"
            }
        )
        
        data = []
        for content in query_result.content:
            if hasattr(content, 'text'):
                data.append(json.loads(content.text))
        
        return data
    
    async def get_accounts(self, limit=50):
        """Get accounts - Order by CreatedDate DESC to show newest first"""
        client = await self.initialize()
        
        query_result = await client.call_tool(
            "query",
            arguments={
                "soql": f"SELECT Id, Name, Phone, Industry, Type, CreatedDate FROM Account ORDER BY CreatedDate DESC LIMIT {limit}"
            }
        )
        
        data = []
        for content in query_result.content:
            if hasattr(content, 'text'):
                data.append(json.loads(content.text))
        
        return data
    
    async def create_account(self, name: str, phone: str = None, industry: str = None):
        """Create account - Following MCP pattern"""
        client = await self.initialize()
        
        fields = {"Name": name}
        if phone:
            fields["Phone"] = phone
        if industry:
            fields["Industry"] = industry
        
        result = await client.call_tool(
            "create",
            arguments={
                "object": "Account",
                "fields": fields
            }
        )
        
        data = []
        for content in result.content:
            if hasattr(content, 'text'):
                data.append(json.loads(content.text))
        
        return data
    
    async def create_contact(self, first_name: str, last_name: str, email: str = None):
        """Create contact - Following MCP pattern"""
        client = await self.initialize()
        
        fields = {
            "FirstName": first_name,
            "LastName": last_name
        }
        if email:
            fields["Email"] = email
        
        result = await client.call_tool(
            "create",
            arguments={
                "object": "Contact",
                "fields": fields
            }
        )
        
        data = []
        for content in result.content:
            if hasattr(content, 'text'):
                data.append(json.loads(content.text))
        
        return data