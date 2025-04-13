import os
import requests
from datetime import datetime


NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DB_ID = os.getenv("NOTION_REPORT_DB_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

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
    title = f"Daily Report – {today.strftime('%Y-%m-%d')}"

    # 🧠 Summary block
    blocks = [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🧠 Summary"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": summary or "No summary available."}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "✅ TODOs"}}]
            }
        }
    ]

    # ✅ To-do blocks
    if todos:
        for todo in todos:
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": f"{todo['task']} (Due: {todo['due_date']})"}}],
                    "checked": False
                }
            })
    else:
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "No TODOs found."}}]
            }
        })

    # 💼 Job Applications section heading
    blocks.append({
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": "💼 Job Applications"}}]
        }
    })

    # 🧱 Table-like entries (column-styled)
    if job_apps:
        for job in job_apps:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": f"• {job['company']} | {job['role']} | {job['status']} | Follow-up: {job['follow_up']}"
                        }
                    }]
                }
            })
    else:
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "No job applications this week."}}]
            }
        })

    # Create the page
    payload = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": blocks
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)

    if response.status_code in [200, 201]:
        print("✅ Report successfully added to Notion!")
    else:
        print(f"❌ Notion API error: {response.status_code}\n{response.text}")
