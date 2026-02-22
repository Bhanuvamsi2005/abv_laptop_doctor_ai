# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
#
# load_dotenv()
#
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#
# # ✅ CORRECT MODEL (FROM YOUR ACCOUNT)
# model = genai.GenerativeModel("models/gemini-2.5-flash")
#
#
# def ask_gemini(problem_text):
#     prompt = f"""
# You are an expert laptop troubleshooting assistant.
#
# User Problem:
# {problem_text}
#
# Provide:
# • Practical troubleshooting steps
# • If hardware issue → suggest repair
# • If replacement needed → suggest product type
#
# Keep response concise and technical.
# """
#
#     response = model.generate_content(prompt)
#
#     return response.text





# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted
#
# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# if not api_key:
#     print("⚠ GEMINI_API_KEY missing")
# else:
#     genai.configure(api_key=api_key)
#
# model = genai.GenerativeModel("models/gemini-2.5-flash")
#
#
# def ask_gemini(problem_text):
#
#     prompt = f"""
# You are an expert laptop troubleshooting assistant.
#
# User Problem:
# {problem_text}
#
# Provide:
# • Practical troubleshooting steps
# • If hardware issue → suggest repair
# • If replacement needed → suggest product type
#
# Keep response concise and technical.
# """
#
#     try:
#         response = model.generate_content(prompt)
#
#         if hasattr(response, "text") and response.text:
#             return response.text
#
#         if hasattr(response, "candidates") and response.candidates:
#             return response.candidates[0].content.parts[0].text
#
#         return "⚠ Empty Gemini response"
#
#     except ResourceExhausted:
#         return "⚠ QUOTA_EXCEEDED"
#
#     except Exception as e:
#         print("Gemini Error:", type(e).__name__, e)
#         return "⚠ GEMINI_FAILURE"


from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, PermissionDenied
import time

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠ CRITICAL: GEMINI_API_KEY not found in .env file")
else:
    print(f"✅ API Key loaded (starts with: {api_key[:8]}...)")
    genai.configure(api_key=api_key)

# Models to try in order of preference
MODEL_OPTIONS = [
    "models/gemini-2.5-flash",  # You have 20/day quota
    "models/gemini-2.0-flash-lite",  # Might have higher quota
    "models/gemini-flash-latest",  # Latest flash model
    "models/gemini-2.0-flash",  # Try this as last resort
]

model = None
model_used = None

for model_name in MODEL_OPTIONS:
    try:
        print(f"Trying model: {model_name}")
        model = genai.GenerativeModel(model_name)
        # Just test with a tiny request to check if it works
        test_response = model.generate_content("Hi", generation_config={"max_output_tokens": 1})
        print(f"✅ Successfully using model: {model_name}")
        model_used = model_name
        break
    except ResourceExhausted as e:
        print(f"⚠ Model {model_name} quota exceeded: {e}")
        continue
    except Exception as e:
        print(f"❌ Model {model_name} failed: {e}")
        continue

if not model:
    print("⚠ No working model found! Using fallback mode.")
    # Use the first model as fallback (will fail gracefully)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    model_used = "models/gemini-2.5-flash"


def ask_gemini(problem_text):
    """
    Get troubleshooting help from Gemini AI
    """
    prompt = f"""You are an expert laptop troubleshooting assistant.

User Problem:
{problem_text}

Provide practical troubleshooting steps in a clear, numbered format.
Keep it concise and technical.
"""

    try:
        print(f"Sending request to Gemini ({model_used}) for: {problem_text[:50]}...")
        response = model.generate_content(prompt)

        # Check for text response
        if hasattr(response, "text") and response.text:
            print("✅ Got response from Gemini")
            return response.text

        # Check candidates (alternative response format)
        if hasattr(response, "candidates") and response.candidates:
            print("✅ Got response from Gemini (candidates format)")
            return response.candidates[0].content.parts[0].text

        print(f"⚠ Unexpected response format: {type(response)}")
        return "⚠ Gemini returned an empty response."

    except ResourceExhausted as e:
        print(f"❌ Quota exceeded: {e}")
        # Return a helpful message
        return """⚠ Gemini API quota exceeded for today.

The free tier allows 20 requests per day for some models.

Please try:
• Wait until tomorrow when quota resets
• Use a different API key
• Or continue using the local knowledge base

Using local troubleshooting for now:"""

    except Exception as e:
        print(f"❌ Gemini Error: {type(e).__name__}: {e}")
        return "⚠ GEMINI_FAILURE"


#
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted
#
# load_dotenv()
#
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#
# model = genai.GenerativeModel("models/gemini-2.5-flash")
#
#
# def ask_gemini(problem_text):
#
#     prompt = f"""
# You are an expert laptop troubleshooting assistant.
#
# User Problem:
# {problem_text}
#
# Provide:
# • Practical troubleshooting steps
# • If hardware issue → suggest repair
# • If replacement needed → suggest product type
#
# Keep response concise and technical.
# """
#
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#
#     except ResourceExhausted:
#         return (
#             "⚠ AI quota temporarily exceeded.\n"
#             "Using local diagnostic intelligence.\n"
#         )
#
#     except Exception as e:
#         print("Gemini Error:", e)
#
#         return (
#             "⚠ AI assistant temporarily unavailable.\n"
#             "Using local troubleshooting engine.\n"
#         )

# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted
#
# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file")
#
# genai.configure(api_key=api_key)
#
# # ✅ Use safest currently stable model
# model = genai.GenerativeModel("gemini-1.5-flash")
#
#
# def ask_gemini(problem_text):
#
#     try:
#         response = model.generate_content(problem_text)
#
#         # ✅ Primary parsing (works most cases)
#         if hasattr(response, "text") and response.text:
#             return response.text
#
#         # ✅ Fallback parsing (Gemini sometimes uses candidates)
#         if hasattr(response, "candidates") and response.candidates:
#             return response.candidates[0].content.parts[0].text
#
#         # ✅ Safety block detection
#         if hasattr(response, "prompt_feedback"):
#             return f"⚠ Response blocked: {response.prompt_feedback}"
#
#         return "⚠ Gemini returned an empty response."
#
#     except ResourceExhausted:
#         return (
#             "⚠ Gemini quota exceeded.\n"
#             "Please check billing / wait for reset."
#         )
#
#     except Exception as e:
#         print("Gemini Error:", type(e).__name__, e)
#
#         return (
#             "⚠ AI assistant temporarily unavailable.\n"
#             "Using fallback system."
#         )
#
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted
#
# load_dotenv()
#
# api_key = os.getenv("GEMINI_API_KEY")
#
# if not api_key:
#     raise ValueError("GEMINI_API_KEY missing")
#
# genai.configure(api_key=api_key)
#
# # ✅ Stable + cheap model
# model = genai.GenerativeModel("gemini-1.5-flash")
#
#
# def ask_gemini(problem_text):
#
#     try:
#         response = model.generate_content(problem_text)
#
#         if hasattr(response, "text") and response.text:
#             return response.text
#
#         if hasattr(response, "candidates") and response.candidates:
#             return response.candidates[0].content.parts[0].text
#
#         return "⚠ Empty Gemini response"
#
#     except ResourceExhausted:
#
#         # ✅ NEVER THROW EXCEPTION
#         return "⚠ QUOTA_EXCEEDED"
#
#     except Exception as e:
#
#         print("Gemini Error:", type(e).__name__, e)
#         return "⚠ GEMINI_FAILURE"
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
#
# load_dotenv()
#
# API_KEY = os.getenv("GEMINI_API_KEY")
#
# if not API_KEY:
#     raise ValueError("GEMINI_API_KEY not found in .env")
#
# genai.configure(api_key=API_KEY)
#
# # ✅ Stable valid model
# model = genai.GenerativeModel("gemini-1.5-flash")
#
#
# def ask_gemini(problem_text):
#     prompt = f"""
# You are an expert laptop troubleshooting assistant.
#
# User Problem:
# {problem_text}
#
# Provide:
# • Practical troubleshooting steps
# • If hardware issue → suggest repair
# • If replacement needed → suggest product type
#
# Keep response concise and technical.
# """
#
#     try:
#         response = model.generate_content(prompt)
#
#         if response and response.candidates:
#             return response.candidates[0].content.parts[0].text
#
#         return "⚠ Empty response from Gemini"
#
#     except Exception as e:
#
#         error_msg = str(e)
#
#         if "quota" in error_msg.lower():
#             return "⚠ QUOTA_EXCEEDED"
#
#         return f"⚠ GEMINI_ERROR: {error_msg}"