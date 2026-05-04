# nodes/writer.py
from langchain_groq import ChatGroq
from state import AgentState
from config import GROQ_API_KEY, GROQ_MODEL
from prompts import COVER_LETTER_PROMPT

CANDIDATE_BACKGROUND = """
I am an AI Engineer and Data Scientist with hands-on experience building production-grade AI systems.

Current roles:
- Research Assistant at ITS Surabaya (AI dept) — building Generative AI models (BERT, TinyBERT) 
  for classification and data generation, managing full data pipelines with Python
- AI Engineer Intern at Chatstat — developed AI assistants and summarizers, built custom agentic 
  workflows, boosted task efficiency by 40% reducing manual intervention
- Data Scientist at Avalon AI Group — designed Multimodal RAG architecture using Llama-4, 
  built full-stack web apps with Multimodal LLMs, implemented PyTorch deep learning models

Previous experience:
- Lecturer Assistant at ITS Surabaya — taught data structures and algorithms, mentored students
- Vice Chairman at Schematics ITS — led 25 members, organised national programming contest 
  with 200+ high school students and 100+ university teams

Core skills: Python, TypeScript, PyTorch, RAG, LLMs, AI Agents, NLP, Full-Stack, Workflow Automation
"""

def writer_node(state: AgentState) -> AgentState:
    print("Writing cover letter...")
    try:
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_MODEL
        )

        prompt = COVER_LETTER_PROMPT.format(
            job_analysis=state["job_analysis"],
            company_research=state["company_research"],
            candidate_background=CANDIDATE_BACKGROUND
        )

        response = llm.invoke(prompt)
        
        cover_letter = response.content

        return {**state, "cover_letter": cover_letter}
    
    except Exception as e:
        return {**state, "error": f"Writer failed: {str(e)}"}

