import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

print("=" * 50)
print("Testing Gemini API Connection...")
print("=" * 50)

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key starts with: {api_key[:8]}...")

# Configure Gemini
genai.configure(api_key=api_key)

# Try the correct model from your list
print("\n" + "=" * 50)
print("Trying models/gemini-2.0-flash...")
print("=" * 50)

try:
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content("What are 3 common laptop problems? Keep it very brief.")
    print(f"✅ SUCCESS! Response:\n{response.text}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")

print("\n" + "=" * 50)
print("Trying models/gemini-2.5-flash...")
print("=" * 50)

try:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content("What are 3 common laptop problems? Keep it very brief.")
    print(f"✅ SUCCESS! Response:\n{response.text}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")