from gmail_utils import get_last_7_days_emails, get_todays_emails
from llm_utils import analyze_emails
from notion_utils import create_weekly_report
from datetime import datetime

def run_weekly_summary_agent():
    print(f"\n📅 Running AI email agent for {datetime.today().strftime('%Y-%m-%d')}")

    # Step 1: Fetch emails
    emails = get_last_7_days_emails()
    print(f"📬 Found {len(emails)} email(s) from the past 7 days.\n")

    if not emails:
        print("❌ No emails to analyze. Skipping report.")
        return

    # Step 2: Analyze with LLM
    summary, todos, job_apps = analyze_emails(emails)

    print("🧠 Summary Preview:")
    print(summary[:300] + "...\n" if summary else "No summary generated.")

    print(f"✅ TODOs: {len(todos)}")
    print(f"💼 Job Applications: {len(job_apps)}")

    # Step 3: Push to Notion
    create_weekly_report(summary, todos, job_apps)

def run_daily_summary_agent():
    print(f"\n📅 Running AI email agent for {datetime.today().strftime('%Y-%m-%d')}")

    # Step 1: Fetch today's emails
    emails = get_todays_emails()
    print(f"📬 Found {len(emails)} email(s) from today.\n")

    if not emails:
        print("❌ No emails to analyze. Skipping report.")
        return

    # Step 2: Analyze with LLM
    summary, todos, job_apps = analyze_emails(emails)

    print("🧠 Summary Preview:")
    print(summary[:300] + "...\n" if summary else "No summary generated.")

    print(f"✅ TODOs: {len(todos)}")
    print(f"💼 Job Applications: {len(job_apps)}")

    # Step 3: Push to Notion
    create_weekly_report(summary, todos, job_apps)

def lambda_handler(event=None, context=None):
    run_daily_summary_agent()