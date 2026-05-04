from tavily import TavilyClient
from state import AgentState
from config import TAVILY_API_KEY

def researcher_node(state: AgentState) -> AgentState:
    """
    Takes company name from job_analysis and searches for company info via Tavily.
    """
    print("Researching company...")

    try:
        company_name = state["job_analysis"]["company_name"]

        client = TavilyClient(api_key=TAVILY_API_KEY)

        results = client.search(
            query=f"{company_name} company culture mission values tech stack",
            max_results=5,
            search_depth="advanced"
        )

        articles = results.get("results", [])

        # stitch all results into one readable block of text
        research_text = "\n\n".join(
            f"- {a['title']}: {a['content'][:300]}"
            for a in articles
        )

        company_research = f"Research on {company_name}:\n{research_text}"

        return {**state, "company_research": company_research}

    except Exception as e:
        return {**state, "error": f"Researcher failed: {str(e)}"}