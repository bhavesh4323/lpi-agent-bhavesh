import requests

BASE_URL = "http://localhost:3333"  # LPI server

def call_tool(endpoint, payload={}):
    response = requests.post(f"{BASE_URL}/{endpoint}", json=payload)
    return response.json()

def run_agent(user_query):
    print(f"\nUser Question: {user_query}\n")

    # 1. Query knowledge
    knowledge = call_tool("query_knowledge", {"query": user_query})

    # 2. Get insights
    insights = call_tool("get_insights", {
        "scenario": user_query,
        "tier": "free"
    })

    # 3. Combine results
    print("=== Agent Answer ===\n")

    print("🔹 Knowledge:")
    print(knowledge.get("results", [])[:1])

    print("\n🔹 Insights:")
    print(insights.get("insights", [])[:1])

    print("\n=== Sources ===")
    print("- query_knowledge tool")
    print("- get_insights tool")


if __name__ == "__main__":
    run_agent("Explain digital twins in simple terms")
