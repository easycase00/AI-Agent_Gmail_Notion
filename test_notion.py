import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# DEBUG: Print loaded env variables
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DB_ID = os.getenv("NOTION_REPORT_DB_ID")

print("🔍 DEBUG - NOTION_API_KEY:", NOTION_API_KEY[:10] + "..." if NOTION_API_KEY else "❌ Not loaded")
print("🔍 DEBUG - NOTION_API_KEY length:", len(NOTION_API_KEY) if NOTION_API_KEY else "❌ Missing")
print("🔍 DEBUG - NOTION_REPORT_DB_ID:", NOTION_DB_ID)

# Set headers
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Mock content for testing
summary = "🧪 This is a test summary of emails from the past week."
todos = [
    {"task": "Submit weekly report", "due_date": "2025-04-14"},
    {"task": "Follow up with recruiter at OpenAI", "due_date": "ASAP"},
]
job_apps = [
    {"company": "Google", "role": "ML Engineer", "status": "applied", "follow_up": "Wait for response"},
    {"company": "Amazon", "role": "Data Scientist", "status": "interview", "follow_up": "Prepare for tech round"},
]

def format_todos(todos):
    if not todos:
        return "No TODOs found."
    return "\n".join([f"• {todo['task']} (Due: {todo['due_date']})" for todo in todos])

def format_job_applications(job_apps):
    if not job_apps:
        return "No job applications this week."
    
    lines = [
        "```",
        f"{'Company':<20} | {'Role':<25} | {'Status':<10} | Follow-up",
        "-" * 75
    ]
    for job in job_apps:
        lines.append(
            f"{job['company']:<20} | {job['role']:<25} | {job['status']:<10} | {job['follow_up']}"
        )
    lines.append("```")
    return "\n".join(lines)

def create_weekly_report(summary: str, todos: list, job_apps: list):
    today = datetime.today()
    title = f"Report – {today.strftime('%Y-%m-%d')}"
    
    print(f"📄 Creating Notion page titled: {title}")

    todo_text = format_todos(todos)
    job_text = format_job_applications(job_apps)

    blocks = [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"type": "text", "text": {"content": "🧠 Summary"}}]}
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": summary}}]}
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"type": "text", "text": {"content": "✅ TODOs"}}]}
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": todo_text}}]}
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {"rich_text": [{"type": "text", "text": {"content": "💼 Job Applications"}}]}
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": job_text}}]}
        }
    ]

    payload = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "Name": {"title": [{"text": {"content": title}}]}
        },
        "children": blocks
    }

    print("📡 Sending request to Notion API...")
    response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)

    print("📬 Response Status:", response.status_code)
    if response.status_code in [200, 201]:
        print("✅ Weekly report successfully added to Notion!")
    else:
        print("❌ Notion API error:")
        print(response.text)

# Run the test
create_weekly_report(summary, todos, job_apps)
