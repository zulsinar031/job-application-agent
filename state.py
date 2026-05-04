from typing import TypedDict, Optional

class AgentState(TypedDict):
    job_url: str                        # input: the job posting URL
    job_raw_content: str                # scraped HTML/text from the URL
    job_analysis: Optional[dict]        # structured: role, requirements, keywords
    company_research: Optional[str]     # Tavily search results about the company
    cover_letter: Optional[str]         # final generated cover letter
    error: Optional[str]                # any error messages