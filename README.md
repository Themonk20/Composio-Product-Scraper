# AI Product Ops Research Engine

Automated API research pipeline built for the **Composio AI Product Ops Intern** take-home assignment.

The goal of this project is to automate the process of researching third-party applications before building AI agent toolkits. Instead of manually inspecting developer documentation, the pipeline crawls official documentation, extracts structured API information using an LLM, and generates research artifacts for further analysis.

---

## Problem Statement

Before building an integration toolkit for an application, several questions need to be answered:

* What does the application do?
* Which authentication methods are supported?
* Is the API publicly available?
* Can developers self-serve API credentials?
* How broad is the API surface?
* Does the application already expose an MCP server?
* Is the application suitable for an AI Agent Toolkit?

Doing this manually across hundreds of applications does not scale.

---

## Solution

This project automates the research workflow using:

* Firecrawl for documentation scraping
* Groq LLM for structured information extraction
* Pydantic for response validation
* Pandas for data storage and analysis
* Python orchestration for automation

The final output is a structured CSV that can be further analyzed to identify integration opportunities and common patterns across SaaS platforms.

---

## Architecture

```text
apps.csv
    │
    ▼
Coordinator
    │
    ▼
Research Agent
    │
    ├── Firecrawl
    │      │
    │      ▼
    │ Documentation
    │
    └── Groq LLM
            │
            ▼
Structured JSON
            │
            ▼
Pydantic Validation
            │
            ▼
results.csv
            │
            ▼
Insights & HTML Report
```

---

## Workflow

1. Read application list from `data/apps.csv`
2. Scrape official API documentation
3. Extract structured metadata using an LLM
4. Validate output using Pydantic
5. Save structured results to CSV
6. Generate insights and final report

---

## Repository Structure

```text
.
├── data/
│   └── apps.csv
│
├── outputs/
│   └── results.csv
│
├── src/
│   ├── coordinator.py
│   ├── research_agent.py
│   ├── firecrawl_service.py
│   ├── llm_service.py
│   ├── models.py
│   ├── storage.py
│   ├── insights.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Themonk20/Composio-Product-Scraper.git
cd Composio-Product-Scraper
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
FIRECRAWL_API_KEY=YOUR_FIRECRAWL_KEY

GROQ_API_KEY=YOUR_GROQ_KEY
```

---

## Run

```bash
python src/main.py
```

---

## Output

The pipeline generates:

```text
outputs/results.csv
```

which contains structured research information for every successfully processed application.

---

## Tech Stack

* Python
* Firecrawl
* Groq
* Pydantic
* Pandas
* Requests
* dotenv

---

## Current Limitations

* Free-tier LLM token limits restricted the number of applications processed in a single execution.
* Some documentation portals returned HTTP 403/404 responses or required authentication.
* Certain enterprise APIs require partner access and cannot be fully evaluated without credentials.

---

## Future Improvements

* Multi-page documentation crawling
* Automatic retry and checkpointing
* Confidence scoring
* Browser-based verification
* Parallel execution
* Native MCP integration
* Automatic HTML report generation

---

## Assignment

Built as part of the **Composio AI Product Ops Intern** take-home assignment.
