from gmail_utils import get_last_7_days_emails
from llm_utils import summarize_email
import json

emails = get_last_7_days_emails()

if not emails:
    print("❌ No emails from the last 7 days.")
    exit()

weekly_summary = ""
todos = []
job_apps = []

print(f"📬 Processing {len(emails)} emails from the last 7 days...\n")

for email in emails:
    try:
        raw = summarize_email(email)
        parsed = json.loads(raw)

        if parsed.get("important"):
            weekly_summary += f"- {parsed['summary']}\n"

        todos.extend(parsed.get("todos", []))

        job = parsed.get("job_application", {})
        if job.get("is_job_related"):
            job_apps.append({
                "company": job["company"],
                "role": job["role"],
                "status": job["status"],
                "follow_up": job.get("follow_up_task", "None")
            })

    except Exception as e:
        print(f"⚠️ Failed to process an email: {e}")

# 🧾 Weekly Report
print("\n====== 🧠 WEEKLY SUMMARY ======\n")
print(weekly_summary.strip() or "No important summaries.")

print("\n====== ✅ TODOs ======\n")
for todo in todos:
    print(f"• {todo['task']} (Due: {todo['due_date']})")

print("\n====== 💼 JOB APPLICATIONS ======\n")
if job_apps:
    print(f"{'Company':<25} | {'Role':<25} | {'Status':<12} | Follow-up")
    print("-" * 80)
    for job in job_apps:
        print(f"{job['company']:<25} | {job['role']:<25} | {job['status']:<12} | {job['follow_up']}")
else:
    print("No job-related emails found.")
