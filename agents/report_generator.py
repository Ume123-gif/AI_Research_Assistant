from tools.search_tool import search
from llm.provider import generate_with_gemini
def generate_report(topic, level):
    if level == "Short":
        words = "500-700 words"
    elif level == "Medium":
        words = "1200-1500 words"
    else:
        words = "2500-3000 words"
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

    Instructions:
    - Write a professional report.
    - Use Markdown.
    - Explain concepts clearly.
    - Include recent developments.
    - Use bullet points where appropriate.
    - If the provided information is insufficient for a section, explicitly state that reliable information was not available instead of making assumptions.
    - Do NOT use information outside the provided sources.
    - Do NOT include raw URLs inside the report body.
    - Make the report suitable for students and professionals.
    - Prefer information from
        - official websites
        - research papers
        - government websites
    - Use Wikipedia only when necessary.
    - Maintain a formal tone.
    - Use citations like [1], [2] after relevant statements.
    - Put all URLs only in the References section.
    - Synthesize information from multiple sources.
    - Avoid repeating the same point.
    - Merge similar ideas into a single coherent explanation.

    Include the following sections:
    Sections:
    # Title
    ## Executive Summary
    ## Overview
    ## Applications
    ## Advantages
    ## Challenges
    ## Recent Developments
    ## Future Scope
    ## Conclusion
    ## References
    [1] ....
    URL
    [2] ....
    URL
    [3] ....
    URL

    Topic: {topic}
    Report Length: {words}
    Information: {context}
    """
    
    report = generate_with_gemini(prompt)
    return report