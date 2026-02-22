# #
# #
# import json
# import numpy as np
# from sentence_transformers import SentenceTransformer
#
# KB_PATH = "kb/knowledge_base.json"
#
# # Load embedding model once (fast after first run)
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
#
# def load_kb():
#     with open(KB_PATH, "r") as f:
#         return json.load(f)
#
#
# def compute_embeddings(kb):
#     issues = [item["issue"] for item in kb]
#     embeddings = model.encode(issues)
#     return issues, embeddings
#
#
# def cosine_similarity(vec1, vec2):
#     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
#
#
# def retrieve_documents(issue_text):
#     kb = load_kb()
#
#     issues, kb_embeddings = compute_embeddings(kb)
#
#     query_embedding = model.encode([issue_text])[0]
#
#     similarities = []
#
#     for emb in kb_embeddings:
#         sim = cosine_similarity(query_embedding, emb)
#         similarities.append(sim)
#
#     best_match_index = np.argmax(similarities)
#     best_score = similarities[best_match_index]
#
#     # Confidence threshold (VERY IMPORTANT)
#     if best_score < 0.45:
#         return []
#
#     return [kb[best_match_index]]
#
# def ask_gemini(problem_text):
#
#     try:
#         print("\n===== GEMINI REQUEST =====")
#         print(problem_text)
#
#         response = model.generate_content(problem_text)
#
#         print("\n===== GEMINI RAW RESPONSE =====")
#         print(response)
#
#         if hasattr(response, "text") and response.text:
#             print("\n===== GEMINI TEXT =====")
#             print(response.text)
#             return response.text
#
#         if hasattr(response, "candidates") and response.candidates:
#             text = response.candidates[0].content.parts[0].text
#             print("\n===== GEMINI CANDIDATE TEXT =====")
#             print(text)
#             return text
#
#         if hasattr(response, "prompt_feedback"):
#             print("\n===== GEMINI BLOCKED =====")
#             print(response.prompt_feedback)
#             return f"⚠ Response blocked: {response.prompt_feedback}"
#
#         return "⚠ Gemini returned an empty response."
#
#     except ResourceExhausted:
#         return "⚠ Gemini quota exceeded."
#
#     except Exception as e:
#         print("\n===== GEMINI ERROR =====")
#         print(type(e).__name__, e)
#
#         return "⚠ AI assistant temporarily unavailable."













import json
import numpy as np
from sentence_transformers import SentenceTransformer

KB_PATH = "kb/knowledge_base.json"

model = SentenceTransformer('all-MiniLM-L6-v2')


def load_kb():
    try:
        with open(KB_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print("KB Load Error:", e)
        return []


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


def retrieve_documents(issue_text):

    try:
        kb = load_kb()

        if not kb:
            return None, 0.0   # ✅ ALWAYS SAFE

        issues = [item["issue"] for item in kb]

        kb_embeddings = model.encode(issues)
        query_embedding = model.encode([issue_text])[0]

        similarities = []

        for emb in kb_embeddings:
            sim = cosine_similarity(query_embedding, emb)
            similarities.append(sim)

        best_match_index = int(np.argmax(similarities))
        best_score = float(similarities[best_match_index])

        if best_score < 0.45:
            return None, best_score   # ✅ SAFE RETURN

        return kb[best_match_index], best_score

    except Exception as e:

        print("Retriever Error:", type(e).__name__, e)

        return None, 0.0   # ✅ NEVER BREAK SYSTEM



















# import json
# import numpy as np
# from sentence_transformers import SentenceTransformer
#
# KB_PATH = "kb/knowledge_base.json"
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
#
# def load_kb():
#     with open(KB_PATH, "r") as f:
#         return json.load(f)
#
#
# def cosine_similarity(vec1, vec2):
#     return np.dot(vec1, vec2) / (
#         np.linalg.norm(vec1) * np.linalg.norm(vec2)
#     )
#
#
# def retrieve_documents(issue_text):
#
#     try:
#         kb = load_kb()
#
#         if not kb:
#             return None, 0.0   # ✅ ALWAYS RETURN TWO VALUES
#
#         issues = [item["issue"] for item in kb]
#
#         kb_embeddings = model.encode(issues)
#         query_embedding = model.encode([issue_text])[0]
#
#         similarities = []
#
#         for emb in kb_embeddings:
#             sim = cosine_similarity(query_embedding, emb)
#             similarities.append(sim)
#
#         best_match_index = int(np.argmax(similarities))
#         best_score = float(similarities[best_match_index])
#
#         if best_score < 0.45:
#             return None, best_score   # ✅ SAFE RETURN
#
#         return kb[best_match_index], best_score
#
#     except Exception as e:
#
#         print("Retriever Error:", type(e).__name__, e)
#
#         # ✅ NEVER BREAK RAG ENGINE
#         return None, 0.0

# import json
# import numpy as np
# from sentence_transformers import SentenceTransformer
#
# KB_PATH = "kb/knowledge_base.json"
#
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
#
# def load_kb():
#     with open(KB_PATH, "r") as f:
#         return json.load(f)
#
#
# def cosine_similarity(vec1, vec2):
#     return np.dot(vec1, vec2) / (
#         np.linalg.norm(vec1) * np.linalg.norm(vec2)
#     )
#
#
# def retrieve_documents(issue_text):
#
#     kb = load_kb()
#
#     if not kb:
#         return None, 0.0
#
#     issues = [item["issue"] for item in kb]
#
#     kb_embeddings = model.encode(issues)
#     query_embedding = model.encode([issue_text])[0]
#
#     similarities = []
#
#     for emb in kb_embeddings:
#         sim = cosine_similarity(query_embedding, emb)
#         similarities.append(sim)
#
#     best_match_index = int(np.argmax(similarities))
#     best_score = float(similarities[best_match_index])
#
#     if best_score < 0.45:
#         return None, best_score
#
#     return kb[best_match_index], best_score