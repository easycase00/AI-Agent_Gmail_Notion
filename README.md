# 📧 Gmail to Notion AI Agent

## 🎯 Motivation

As a data-driven individual in a fast-paced, information-dense world, I found myself constantly overwhelmed by the volume and variability of emails hitting my inbox—especially while actively job hunting and coordinating multiple threads of professional communication. Manually parsing through emails, identifying action items, and tracking job applications became not only tedious but error-prone.

This project was born out of a personal need to **automate cognitive overhead** and maintain a high degree of **personal operational efficiency**. I wanted a system that could:

- Surface only **high-signal, actionable information** from my Gmail.
- Automatically **extract TODOs**, replies, follow-ups, and job-related activity.
- Maintain an **ongoing daily log of professional activity**, searchable and organized in Notion.
- Be **production-grade**, **scalable**, and **cloud-native** so I could depend on it—without manual intervention.

It combines **natural language processing**, **intelligent summarization**, and **automated task structuring** to keep me focused on high-value actions—not inbox management. Think of it as an AI-powered **personal chief of staff**, handling the mundane so I can focus on what matters.

---

## 📌 Project Overview

This agent seamlessly connects **Gmail**, **Groq’s state-of-the-art LLaMA 3.3 (70B Versatile)** language model, and **Notion**, delivering automated, daily summarized reports directly from my inbox. Built on robust serverless infrastructure using **AWS Lambda** and **Amazon EventBridge**, this tool organizes emails into concise summaries, actionable TODOs, and structured job application tracking.

---

## 🛠️ Technical Architecture

The system integrates the following key components:

### 1. **Gmail API (Google Cloud)**
- OAuth 2.0 authentication.
- Daily retrieval of emails.
- Extraction of email metadata and content parsing via Google APIs and base64 encoding.

### 2. **Natural Language Processing with Groq**
- Leveraged GroqCloud’s powerful LLaMA 3.3 (70B Versatile) language model.
- Summarizes emails and classifies actionable insights using prompt engineering.
- Extracts specific structured details (summary, TODOs, job applications).

### 3. **Notion Integration**
- Utilizes Notion's powerful API to dynamically generate structured and interactive daily reports.
- Clearly structured reports include:
  - Concise summaries of essential emails.
  - Interactive checkboxes for TODOs.
  - Structured tables for job applications, statuses, and follow-ups.

### 4. **AWS Lambda (Serverless Deployment)**
- Serverless deployment for maximum scalability and cost efficiency.
- Robust environment variables handling for secure credentials.
- Zero management infrastructure—automatic scaling and reliability.

### 5. **Amazon EventBridge (Automated Scheduling)**
- Event-driven serverless architecture for daily invocation at precisely 7:00 PM.
- Automated, reliable, and maintenance-free execution pipeline.

---

## 🚀 Workflow

- **Email Fetching**: Daily, the agent securely retrieves emails from Gmail via Google’s API.
- **LLM-based Summarization**: Utilizes GroqCloud’s API to intelligently summarize and analyze emails.
- **Notion Reporting**: Parsed data populates into a structured Notion database, making content organized, actionable, and clear.
- **Automation via AWS**: Automated invocation using AWS Lambda triggered by Amazon EventBridge.

---

## ⚙️ Implementation Details & Tech Stack

| Layer          | Tool/Service                | Role                                                   |
|----------------|-----------------------------|--------------------------------------------------------|
| **Email**      | Gmail API                   | Fetch and read emails                                  |
| **LLM**        | Groq Cloud + LLaMA 3.3 70B  | Fast contextual summarization & job detection          |
| **Backend**    | Python + Lang-style routing | Modular agent framework for orchestration              |
| **Database**   | Notion API                  | Logs daily summaries, todos, and job applications      |
| **Cloud**      | AWS Lambda + EventBridge    | Scheduled daily pipeline execution at 7PM              |


---

## 📊 Results & Efficiency

The agent delivers significant productivity improvements:

- ✅ **Email Summarization**: Transforms 20+ daily emails into clear 1-line summaries.
- ✅ **Job Applications Tracking**: Tracks over 19 job-related emails weekly, clearly listing their statuses and actionable next steps.
- ✅ **Task Automation**: Automatically generates interactive TODOs, significantly reducing manual task management.


## 🖥️ Sample Output, Deployment Proofs & Screenshots


### ✅ Terminal Output (Local Agent Run)
![Terminal Output](https://github.com/easycase00/AI-Agent_Gmail_Notion/blob/main/SS/Screenshot%202025-04-13%20at%205.15.24%E2%80%AFPM.png)

---

### ✅ AWS Lambda Execution (Cloud Deployment)
![AWS Lambda Log Output](https://github.com/easycase00/AI-Agent_Gmail_Notion/blob/main/SS/Screenshot%202025-04-13%20at%205.58.26%E2%80%AFPM.png)

---

### ✅ AWS EventBridge Scheduler (CRON Trigger Setup)
![AWS EventBridge Scheduler](https://github.com/easycase00/AI-Agent_Gmail_Notion/blob/main/SS/Screenshot%202025-04-13%20at%206.07.02%E2%80%AFPM.png)

---

### ✅ Notion Report Output (Daily Page Structure)
![Notion Output](https://github.com/easycase00/AI-Agent_Gmail_Notion/blob/main/SS/Screenshot%202025-04-13%20at%206.08.52%E2%80%AFPM.png)

---

## 🚧 Future Enhancements

- **Advanced Analytics**: Add predictive capabilities for actionable reminders (e.g., anticipated interview preparation).
- **Extended Integrations**: Further integrations with calendar and task management tools (e.g., Google Calendar, Todoist).
- **Enhanced Security**: Implement AWS Secrets Manager for more secure credentials handling.

---

## 💼 Professional Impact

- Dramatically improved inbox management, saving hours of manual processing weekly.
- Enabled rigorous tracking of job applications, resulting in a more strategic and effective job search process.
- Showcased advanced NLP and cloud deployment skills in a real-world, practical scenario—highly appealing for recruiters and employers.

---

## 📖 How to Run the Project Locally

```bash
# Clone repository
git clone https://github.com/easycase00/AI-Agent_Gmail_Notion.git
cd AI-Agent_Gmail_Notion

# Install dependencies
pip install -r requirements.txt

# Set environment variables (.env)
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
NOTION_API_KEY=your_notion_api_key
NOTION_REPORT_DB_ID=your_notion_db_id

# Run local agent
python main.py
```

---

## 🔗 **Repository Structure**

AI-Agent_Gmail_Notion
├── main.py                 # Entry-point script
├── gmail_utils.py          # Gmail API interaction
├── llm_utils.py            # GroqCloud NLP model interaction
├── notion_utils.py         # Notion API interaction
├── requirements.txt        # Python package dependencies
├── .env                    # Environment Variables (secured)
└── assets                  # Screenshots and proof images
