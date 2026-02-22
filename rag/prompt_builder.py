def build_prompt(company, model, user_problem, retrieved_docs):
    context = ""

    for doc in retrieved_docs:
        context += f"Issue: {doc['issue']}\n"
        context += "Solutions:\n"
        for sol in doc["solutions"]:
            context += f"- {sol}\n"
        context += "\n"

    prompt = f"""
You are an enterprise IT support assistant.

Laptop Company: {company}
Laptop Model / OS: {model}

User Problem:
{user_problem}

Relevant Knowledge Base Information:
{context}

Instructions:
Provide a clear, step-by-step troubleshooting solution.
Be concise, practical, and technical.
Do not invent solutions outside the provided knowledge.
"""

    return prompt