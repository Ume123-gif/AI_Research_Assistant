from tools.search_tool import search
def generate_report(topic, level):
    search_result = search(topic)
    report = f"""# {topic}

## Overview
This is the overview.

## Applications
Applications of {topic}.

## Challenges
Challenges of {topic}.

## Future Scope
Future scope of {topic}.

## Conclusion
Conclusion
"""
    return report