from gmail_utils import get_today_emails

emails = get_today_emails()

print(f"📬 Found {len(emails)} email(s) today.")
for i, email in enumerate(emails, 1):
    print(f"\n--- Email {i} ---")
    print(f"From: {email['from']}")
    print(f"Subject: {email['subject']}")
    print(f"Body:\n{email['body'][:300]}...\n")
