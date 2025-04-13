import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

def summarize_email(email):
    prompt = f"""
You are an intelligent assistant summarizing a week's worth of emails one at a time.

Given the email below, return the following:
1. Whether the email is important.
2. A 1-line summary.
3. A list of TODOs (e.g., reply, follow-up, prepare, schedule).
4. If the email is job-related, extract:
   - Company
   - Role
   - Application status: applied / interview / offer / rejected / other
   - Follow-up task (if any)

Respond in this JSON format:
{{
  "important": true or false,
  "summary": "One-line summary",
  "todos": [
    {{
      "task": "Task description",
      "due_date": "YYYY-MM-DD or ASAP"
    }}
  ],
  "job_application": {{
    "is_job_related": true or false,
    "company": "Company name",
    "role": "Job title",
    "status": "applied/interview/offer/rejected/other",
    "follow_up_task": "Action needed (if any)"
  }}
}}

Email:
Subject: {email['subject']}
From: {email['from']}
Body:
{email['body']}
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": GROQ_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
    )

    return response.json()['choices'][0]['message']['content']

def analyze_emails(emails):
    summaries = []
    todos = []
    job_apps = []

    for email in emails:
        try:
            raw = summarize_email(email)
            parsed = json.loads(raw)

            if parsed.get("important"):
                summaries.append(f"- {parsed.get('summary')}")

            todos.extend(parsed.get("todos", []))

            job = parsed.get("job_application", {})
            if job.get("is_job_related"):
                job_apps.append({
                    "company": job.get("company"),
                    "role": job.get("role"),
                    "status": job.get("status"),
                    "follow_up": job.get("follow_up_task", "None")
                })

        except Exception as e:
            print("⚠️ Error processing email:", email['subject'])
            print(e)

    summary_text = "\n".join(summaries)
    return summary_text, todos, job_apps
