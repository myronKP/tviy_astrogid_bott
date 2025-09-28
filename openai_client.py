import os
from openai import AsyncOpenAI

# Read API key from environment variable OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

# Single shared async client
client = AsyncOpenAI(api_key=api_key)
