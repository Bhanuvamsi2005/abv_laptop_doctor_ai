import re

def extract_issue(problem_text):
    text = problem_text.lower()

    cleaned = re.sub(r'[^a-z0-9\s]', '', text)

    return {
        "original": problem_text,
        "normalized": cleaned
    }