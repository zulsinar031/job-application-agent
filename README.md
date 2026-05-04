# 🤖 Job Application Agent

> Paste a job posting URL — get a tailored cover letter in seconds.

![LangGraph](https://img.shields.io/badge/LangGraph-1.1.10-purple)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange)
![Tavily](https://img.shields.io/badge/Tavily-Search%20%2B%20Extract-blue)
![Docker](https://img.shields.io/badge/Docker-containerized-2496ED)
![Python](https://img.shields.io/badge/Python-3.11-yellow)

---

## 🧠 What it does

Most cover letters are generic. This agent reads the actual job posting, researches the company, and writes a cover letter that mirrors the role's keywords and reflects the company's culture — all in under 30 seconds.

---

## 🔀 Agent Flow

```
Job URL
   │
   ▼
┌─────────────┐
│  scraper    │  Tavily extracts clean text from the job posting URL
└──────┬──────┘
       │ job_raw_content
       ▼
┌─────────────┐
│  analyzer   │  Groq reads the posting → returns structured JSON
└──────┬──────┘  (company, role, requirements, keywords, culture)
       │ job_analysis
       ▼
┌─────────────┐
│ researcher  │  Tavily searches the web for company info
└──────┬──────┘  (mission, values, news, tech stack)
       │ company_research
       ▼
┌─────────────┐
│   writer    │  Groq combines everything + your background
└──────┬──────┘  → generates tailored cover letter
       │
       ▼
 cover_letter.txt
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Agent orchestration & state management |
| [Groq](https://groq.com) | Fast LLM inference (llama-3.3-70b-versatile) |
| [Tavily](https://tavily.com) | Job posting extraction + company research |
| [LangChain](https://langchain.com) | LLM client abstractions |
| [Docker](https://docker.com) | Containerized runtime |

---

## 🚀 How to run

### 1. Clone the repo
```bash
git clone https://github.com/zulsinar031/job-application-agent.git
cd job-application-agent
```

### 2. Set up your API keys
Create a `.env` file in the root:
```env
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

Get your keys here:
- Groq: https://console.groq.com
- Tavily: https://app.tavily.com

### 3. Update your background
Open `nodes/writer.py` and update `CANDIDATE_BACKGROUND` with your own experience.

### 4. Build the Docker image
```bash
docker-compose build
```

### 5. Run the agent
```bash
docker-compose run job-agent
```

Paste any job posting URL when prompted:
```
🚀 Job Application Agent
========================================
Paste job posting URL: https://id.jobstreet.com/id/job/91581927
```

### 6. Get your cover letter
The cover letter is printed to terminal and saved to:
```
outputs/cover_letter_COMPANY_NAME.txt
```

---

## 📄 Example Output

```
========================================
📄 YOUR COVER LETTER
========================================
Dear Hiring Manager at KAZOKKU,

I was impressed to learn about KAZOKKU's commitment to providing tailored 
IT talent solutions that cater to the unique needs of each project. As an 
AI Engineer and Data Scientist with a passion for building production-grade 
AI systems, I am excited about the opportunity to join your team...

[full cover letter]
========================================

📊 JOB ANALYSIS SUMMARY
========================================
Company:  KAZOKKU
Role:     AI Engineer
Keywords: AI, ML, Deep Learning, LLM, MLOps, Docker, Kubernetes, AWS, GCP, Azure

💾 Saved to outputs/cover_letter_KAZOKKU.txt
```

---

## 📁 Project Structure

```
job-application-agent/
├── nodes/
│   ├── scraper.py       # Tavily URL extraction
│   ├── analyzer.py      # Groq JSON analysis
│   ├── researcher.py    # Tavily company research
│   └── writer.py        # Groq cover letter generation
├── state.py             # Shared LangGraph state
├── graph.py             # Node wiring & conditional edges
├── config.py            # API keys & model settings
├── prompts.py           # All LLM prompts
├── main.py              # Entrypoint
├── outputs/             # Generated cover letters (gitignored)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ⚠️ Notes

- Works best with direct job posting URLs (Greenhouse, Lever, Jobstreet, Workday)
- Avoid job board search pages — use individual job posting URLs
- LinkedIn job postings may be blocked due to login requirements
- The agent does **not** submit applications — it only generates the cover letter
