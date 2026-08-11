import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ No API key found in .env")
    exit(1)

genai.configure(api_key=api_key)

print("🔍 Querying Google's servers for available models...")
try:
    models = genai.list_models()
    count = 0
    for m in models:
        if "generateContent" in m.supported_generation_methods:
            print(f"✅ Found model: {m.name}")
            count += 1
    
    if count == 0:
        print("❌ No models found that support text generation for this API key.")
except Exception as e:
    print(f"❌ API Error: {e}")
