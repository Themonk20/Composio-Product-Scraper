import os
import json
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from models import AppResearch

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze(app_name, documentation, docs_url):

    prompt = f"""
You are an API research assistant.

Research the following application using ONLY the provided documentation.

Return ONLY valid JSON.

Application:
{app_name}

Documentation:
{documentation[:25000]}

Official Documentation URL:
{docs_url}

Return JSON with exactly these fields:

{{
"name":"",
"category":"",
"description":"",
"auth_methods":[],
"self_serve":"",
"api_type":"",
"api_scope":"",
"mcp_available":false,
"buildable":true,
"blocker":"",
"evidence":["{docs_url}"],
"toolkit_priority":"",
"integration_difficulty":""
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    result = response.choices[0].message.content

    data = json.loads(result)

    value = data.get("self_serve")

    if isinstance(value, bool):
     data["self_serve"] = "Yes" if value else "No"

    elif value is None:
     data["self_serve"] = "UNKNOWN"

    else:
     data["self_serve"] = str(value)

    return AppResearch(**data)