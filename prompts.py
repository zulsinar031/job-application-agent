ANALYZE_JOB_PROMPT = """
You are a job posting analyzer. Extract the following from the job posting below and return as JSON:

- company_name: string
- role_title: string  
- requirements: list of strings
- nice_to_have: list of strings
- keywords: list of strings (important words to mirror in cover letter)
- company_culture: string (any hints about culture, values, tone)

Job posting:
{job_content}

Return ONLY valid JSON. No explanation, no markdown.
"""

RESEARCH_SUMMARY_PROMPT = """
You are summarizing company research for a job applicant.
Based on the search results below, write a concise summary covering:

- What the company does
- Their mission or values
- Recent news or notable achievements
- Tech stack or tools they use (if mentioned)
- Culture or work environment clues

Search results:
{search_results}

Keep it under 300 words. Write in plain paragraphs, no bullet points.
"""

COVER_LETTER_PROMPT = """
You are an expert cover letter writer. Write a tailored, professional cover letter.

Job Analysis:
{job_analysis}

Company Research:
{company_research}

Candidate Background:
{candidate_background}

Instructions:
- Open with a strong hook that shows you know the company
- Mirror keywords from the job posting naturally
- Connect the candidate's experience to the role's requirements
- Show genuine enthusiasm based on the company research
- Keep it under 400 words
- Professional but human tone — not robotic
- Do NOT use generic phrases like "I am writing to apply for..."
"""