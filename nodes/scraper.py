from tavily import TavilyClient
from state import AgentState
from config import TAVILY_API_KEY

def scraper_node(state: AgentState) -> AgentState:
    """
    Takes the job URL from state and extracts clean text using Tavily.
    """
    print("Scraping job posting...")
    
    try:
        client = TavilyClient(api_key=TAVILY_API_KEY)
        
        response = client.extract(urls=[state["job_url"]])
        
        # Tavily returns a list of results, we grab the first one
        raw_content = response["results"][0]["raw_content"]
        
        return {**state, "job_raw_content": raw_content}
    
    except Exception as e:
        return {**state, "error": f"Scraper failed: {str(e)}"}