import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(csv_text: str):

    prompt = f"""
You are an AI Product Operations Analyst.

You are given integration research results.

Write an executive summary.

Answer:

1. Most common authentication method
2. Which categories are easiest to integrate?
3. Which categories are hardest?
4. Most common blocker
5. How many apps are self-serve?
6. How many appear to be high-priority integrations?
7. Top 5 insights for Composio.

Keep it concise.
Use bullet points.

Dataset:

{csv_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text