from tools.search_tool import search
from llm.provider import generate_with_gemini
def generate_report(topic, level):
    search_result = search(topic)
    context = ""
    for result in search_result:
        context += f"""
        Topic: {result["title"]}
        Content: {result["content"]}
        Source: {result["url"]}
    """
    prompt = f"""
    You are an expert research assistant.
    Using ONLY the information provided below, generate a well-structured Markdown report.
    Topic: {topic}
    Report Length: {level}

    Include the following sections:
    # {topic}

    ## Overview

    ## Applications

    ## Challenges

    ## Future Scope

    ## Conclusion

    Research Material:
    {context}
    """
    report = generate_with_gemini(prompt)
    return report