"""
Test Salesforce connection independently
"""
from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

print("🧪 Testing Salesforce Connection...\n")

username = os.getenv("SALESFORCE_USERNAME")
password = os.getenv("SALESFORCE_PASSWORD")
token = os.getenv("SALESFORCE_SECURITY_TOKEN")
domain = os.getenv("SALESFORCE_DOMAIN", "login").replace("https://", "").replace(".salesforce.com", "")

print(f"Username: {username}")
print(f"Password: {'*' * len(password) if password else 'NOT SET'}")
print(f"Token: {'*' * len(token) if token else 'NOT SET'}")
print(f"Domain: {domain}\n")

if not username or not password or not token:
    print("❌ Missing credentials in .env file!")
    exit(1)

try:
    sf = Salesforce(
        username=username,
        password=password,
        security_token=token,
        domain=domain
    )
    
    print("✅ Connection successful!")
    
    # Try a simple query
    result = sf.query("SELECT Id, Name FROM Contact LIMIT 1")
    print(f"✅ Query successful! Found {result['totalSize']} contacts")
    
    if result['records']:
        print(f"   Sample: {result['records'][0].get('Name', 'No name')}")
    
except Exception as e:
    print(f"❌ Connection failed!")
    print(f"   Error: {str(e)}\n")
    
    print("📋 Troubleshooting steps:")
    print("1. Go to Salesforce → Settings → Reset My Security Token")
    print("2. Check email for new token")
    print("3. Update .env with new token")
    print("4. Make sure SALESFORCE_DOMAIN=login (not the full URL)")
    print("5. Verify password is correct")