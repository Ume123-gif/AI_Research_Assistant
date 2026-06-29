import os
from tavily import TavilyClient
client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))
response = client.search(
    query = "Quantum Computing",
    search_depth = "advanced"
)
for result in response["results"]:
    print("Title : ", result["title"])
    print("Link : ", result["url"])
    print("Content : ", result["content"])
    print("-" * 100)