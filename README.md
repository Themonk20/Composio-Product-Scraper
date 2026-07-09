# API Intelligence Agent

### Automated API Research Pipeline for AI Agent Toolkit Development

Built as part of the **Composio AI Product Ops Intern Take-Home Assignment**.

---

# Overview

Before Composio builds an AI toolkit for an application, it needs to understand the application's developer ecosystem:

* What does the application do?
* Which authentication methods are supported?
* Is the API publicly available?
* Can developers self-serve credentials?
* How extensive is the API surface?
* Does the platform already expose an MCP server?
* Is the application suitable for an AI agent toolkit?

Researching this manually across hundreds of SaaS applications is slow and difficult to scale.

This project automates a large portion of that research workflow by scraping official documentation, extracting structured API metadata using an LLM, validating the output, and storing the results in a machine-readable format.

---

# Features

* Automated documentation scraping
* Structured API metadata extraction
* Authentication detection
* API surface classification
* Buildability assessment
* MCP availability detection
* CSV-based research output
* Retry mechanism for failed requests
* Resume support for interrupted runs

---

# Architecture

```text
                    apps.csv
                        │
                        ▼
                Coordinator Agent
                        │
                        ▼
                Research Agent
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
Documentation Scraper              Groq LLM
(Requests + BeautifulSoup)    (Structured Extraction)
        │                               │
        └───────────────┬───────────────┘
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

# Workflow

1. Read the list of applications from `data/apps.csv`
2. Visit the official developer documentation
3. Scrape relevant documentation content
4. Send the documentation to Groq for structured extraction
5. Validate the extracted fields using Pydantic
6. Save structured research results to CSV
7. Generate insights and reports

---

# Repository Structure

```text
.
├── data
│   └── apps.csv
│
├── outputs
│   └── results.csv
│
├── src
│   ├── coordinator.py
│   ├── research_agent.py
│   ├── scraper.py
│   ├── llm_service.py
│   ├── models.py
│   ├── storage.py
│   ├── insights.py
│   ├── report_generator.py
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

# Tech Stack

* Python
* Requests
* BeautifulSoup4
* Groq API
* Pydantic
* Pandas
* python-dotenv

---

# Installation

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

Windows

```bash
venv\\Scripts\\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Running the Project

Run the pipeline

```bash
python src/main.py
```

The pipeline will:

* Read applications from `data/apps.csv`
* Scrape documentation
* Extract structured information
* Save results into

```text
outputs/results.csv
```

---

# Output Schema

Each application contains the following fields:

| Field                  | Description                        |
| ---------------------- | ---------------------------------- |
| name                   | Application name                   |
| category               | Product category                   |
| description            | One-line summary                   |
| auth_methods           | Authentication methods             |
| self_serve             | Whether credentials are self-serve |
| api_type               | REST / GraphQL / Other             |
| api_scope              | API coverage                       |
| mcp_available          | MCP support                        |
| buildable              | Suitable for toolkit               |
| blocker                | Integration blocker                |
| evidence               | Documentation URL                  |
| toolkit_priority       | Estimated integration priority     |
| integration_difficulty | Easy / Medium / Hard               |

---

# Verification

To improve reliability:

* Information is extracted only from official documentation.
* Structured responses are validated using Pydantic.
* Failed requests are retried automatically.
* The pipeline can resume from previously completed applications.
* Manual spot-checks can be performed against the documentation links stored in the output.

---

# Current Limitations

* The submission was executed using free-tier LLM access, which limited the number of applications processed in a single run due to token quotas.
* Some documentation portals returned HTTP 403 or 404 responses.
* Certain enterprise APIs require authentication or partner access.
* Some documentation websites required manual verification because of restricted access or non-standard documentation layouts.

---

# Future Improvements

* Browser-based documentation extraction
* Multi-page crawling
* Automatic confidence scoring
* Parallel processing
* Incremental updates
* Better authentication detection
* Automatic HTML report generation
* Native MCP integration
* Browser-use verification agent
* Continuous synchronization for documentation changes

---

# Assignment Context

This project was developed for the **Composio AI Product Ops Intern Take-Home Assignment**.

The objective was to automate the research process required before building AI agent toolkits by transforming unstructured API documentation into structured, actionable metadata.

The implementation focuses on automation, structured extraction, reproducibility, and transparent reporting while acknowledging the practical constraints of free-tier API usage.
