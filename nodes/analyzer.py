# nodes/analyzer.py
import json
from langchain_groq import ChatGroq
from state import AgentState
from config import GROQ_API_KEY, GROQ_MODEL
from prompts import ANALYZE_JOB_PROMPT

def analyzer_node(state: AgentState) -> AgentState:
    print("🧠 Analyzing job posting...")

    try:
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_MODEL
        )

        prompt = ANALYZE_JOB_PROMPT.format(
            job_content=state["job_raw_content"]
        )

        response = llm.invoke(prompt)
        
        # strip markdown code blocks if Groq wraps response in them
        content = response.content.strip()
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        content = content.strip()

        job_analysis = json.loads(content)

        return {**state, "job_analysis": job_analysis}

    except json.JSONDecodeError as e:
        return {**state, "error": f"Analyzer failed: Groq did not return valid JSON: {str(e)}"}
    except Exception as e:
        return {**state, "error": f"Analyzer failed: {str(e)}"}