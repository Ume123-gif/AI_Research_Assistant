import os
from tavily import TavilyClient 
def search(topic):
    try:
        client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))
        response = client.search(
        query = f"{topic}",
        search_depth = "advanced"
        )
        search_result = []
        for result in response["results"]:
            res = {}
            res["title"] = result["title"]
            res["url"] = result["url"]
            res["content"] = result["content"]
            search_result.append(res)
        return search_result
    except Exception as e:
        print("Cannot retrieve information from the web!", e)