import os
import traceback
from dotenv import load_dotenv
load_dotenv()

print("GEMINI KEY FOUND:", "GEMINI_API_KEY" in os.environ)
print("KEY:", os.environ.get("GEMINI_API_KEY", "NOT SET"))

import litellm
litellm.set_verbose = True

from crewai import LLM

llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.2)

try:
    response = llm.call([{"role": "user", "content": "Say hello"}])
    print("✅ LLM WORKS:", response)
except Exception as e:
    print("❌ FULL ERROR:")
    traceback.print_exc()