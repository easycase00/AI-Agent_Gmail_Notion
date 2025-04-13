import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv(dotenv_path=Path('.') / '.env')

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_REPORT_DB_ID = os.getenv("NOTION_REPORT_DB_ID")



# DEBUG
print("Loaded NOTION_API_KEY:", NOTION_API_KEY[:10] + "..." if NOTION_API_KEY else "None")
print("Loaded NOTION_REPORT_DB_ID:", NOTION_REPORT_DB_ID)

url = f"https://api.notion.com/v1/databases/{NOTION_REPORT_DB_ID}/query"
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

print("URL:", url)
print("Headers:", headers)


response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("✅ Connected to Notion successfully!\n")
    data = response.json()
    results = data.get("results", [])

    if not results:
        print("📂 No pages found in the database.")
    else:
        print("📄 Page Titles:")
        for page in results:
            props = page.get("properties", {})
            title_prop = next(
                (v for v in props.values() if v.get("type") == "title"), None
            )
            if title_prop and title_prop["title"]:
                title = title_prop["title"][0]["text"]["content"]
                print(f" - {title}")
else:
    print(f"❌ Failed to connect. Status code: {response.status_code}")
    print("Response:", response.text)
