from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.scraper import scraper_node
from nodes.analyzer import analyzer_node
from nodes.researcher import researcher_node
from nodes.writer import writer_node

def should_continue(state: AgentState) -> str:
    """
    Check if there's an error after each node.
    If yes, stop the graph. If no, keep going.
    """
    if state.get("error"):
        return "end"
    return "continue"

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("scraper", scraper_node)
    graph.add_node("analyzer", analyzer_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)

    graph.set_entry_point("scraper")
    graph.add_conditional_edges(
        "scraper",
        should_continue,
        {"continue": "analyzer", "end": END}
    )
    graph.add_conditional_edges(
        "analyzer",
        should_continue,
        {"continue": "researcher", "end": END}
    )
    graph.add_conditional_edges(
        "researcher",
        should_continue,
        {"continue": "writer", "end": END}
    )
    graph.add_edge("writer", END)

    return graph.compile()