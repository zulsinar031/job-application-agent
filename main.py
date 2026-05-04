import os
from graph import build_graph

def main():
    print("🚀 Job Application Agent")
    print("=" * 40)
    
    job_url = input("Paste job posting URL: ").strip()
    
    if not job_url:
        print("❌ No URL provided")
        return
    
    initial_state = {
        "job_url": job_url,
        "job_raw_content": None,
        "job_analysis": None,
        "company_research": None,
        "cover_letter": None,
        "error": None
    }
    
    graph = build_graph()
    
    print("\n⏳ Running agent...\n")
    final_state = graph.invoke(initial_state)
    
    if final_state.get("error"):
        print(f"❌ Agent failed: {final_state['error']}")
        return
    
    print("=" * 40)
    print("📄 YOUR COVER LETTER")
    print("=" * 40)
    print(final_state["cover_letter"])
    print("=" * 40)

    print("\n📊 JOB ANALYSIS SUMMARY")
    print("=" * 40)
    analysis = final_state["job_analysis"]
    print(f"Company:  {analysis['company_name']}")
    print(f"Role:     {analysis['role_title']}")
    print(f"Keywords: {', '.join(analysis['keywords'])}")

    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/cover_letter_{analysis['company_name'].replace(' ', '_')}.txt"
    with open(filename, "w") as f:
        f.write(f"Company: {analysis['company_name']}\n")
        f.write(f"Role: {analysis['role_title']}\n")
        f.write("=" * 40 + "\n\n")
        f.write(final_state["cover_letter"])

    print(f"\n💾 Saved to {filename}")

if __name__ == "__main__":
    main()